# -*- coding: utf-8 -*-
#
from selenium import webdriver
import time
import os.path
import multiprocessing as mp


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


if __name__ == '__main__':
    t = time.time()
    get_dir()
    urls = readtxt()
    pool = mp.Pool(processes=10)
    pool.map_async(func=webshot, iterable=urls)
    pool.close()
    pool.join()
    print("操作结束，耗时：{:.2f}秒".format(float(time.time() - t)))
