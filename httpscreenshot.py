# -*- coding: utf-8 -*-
#
from datetime import datetime
import time
import os.path
import multiprocessing as mp
from selenium import webdriver


HTML_HEAD = '''\
<html>

<head>
    <title>Web Application Catalog</title>
    <link href="style.css" rel="stylesheet" type="text/css">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Refresh" content="60" ;/>
</head>

<body>
'''

HTML_TABLE = '''
<div class="table">
    <table class="table-fill">
        <thead>
        <TR>
            <th class="text-left">
                {title}
            </th>
        </TR>
        </thead>
        <TR>
            <TD><a href="{href}" target="_blank"><img src="pics/{pic_name}.png" width=150 height=150/></a></TD>
        </TR>
    </table>
</div>
'''

HTML_FOOTER = '''
<span class="footer">
    {screenshot_updated_time}
</span>
</body>
</html>
'''


def readtxt():
    """读取txt文件，返回一个列表，每个元素都是一个元组;文件的格式是图片保存的名称加英文逗号加网页地址"""
    with open('urls.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    urls = []
    for line in lines:
        try:
            thelist = line.strip().split(",")
            if len(thelist) == 3 and thelist[1] and thelist[2]:
                urls.append((thelist[1], thelist[2]))
        except:
            pass
    return urls


def get_dir():
    """判断文件夹是否存在，如果不存在就创建一个"""
    filename = "pics"
    if not os.path.isdir(filename):
        os.makedirs(filename)
    return filename


def webshot(tup):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # 返回网页的高度的js代码
    js_height = "return document.body.clientHeight"
    picname = str(tup[0])

    link = tup[1]
    try:
        driver.get(link)
        k = 1
        height = driver.execute_script(js_height)
        while True:
            if k * 500 < height:
                js_move = "window.scrollTo(0,{})".format(k * 500)
                print(js_move)
                driver.execute_script(js_move)
                time.sleep(0.2)
                height = driver.execute_script(js_height)
                k += 1
            else:
                break
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(scroll_width, scroll_height)
        driver.get_screenshot_as_file("pics/" + picname + ".png")
        print("Process {} get one pic !!!".format(os.getpid()))
        time.sleep(0.1)
    except Exception as e:
        print(picname, e)
        driver.quit()
    driver.close()
    driver.quit()


def index_page_gen(updated_time):
    content = HTML_HEAD
    with open('index.html', 'w', encoding='utf-8') as index_page:
        with open('urls.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            try:
                thelist = line.strip().split(",")
                if len(thelist) == 3:
                    content += HTML_TABLE.format(title=thelist[0], href=thelist[2], pic_name=thelist[1])
            except:
                pass
        index_page.write(content + HTML_FOOTER.format(screenshot_updated_time=updated_time))


if __name__ == '__main__':
    t = time.time()
    get_dir()
    urls = readtxt()
    pool = mp.Pool(processes=10)
    pool.map_async(func=webshot, iterable=urls)
    pool.close()
    pool.join()
    print("操作结束，耗时：{:.2f}秒".format(float(time.time() - t)))
    index_page_gen(datetime.now())
