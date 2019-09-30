# -*- coding: utf-8 -*-
#
import datetime

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
    main()