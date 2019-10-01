# httpscreenshot

1、pip install -r requirement.txt -i https://pypi.douban.com/simple

2、查看本机Chrome版本，去http://npm.taobao.org/mirrors/chromedriver 下载对应版本的webdriver。放置于venv/Scripts目录中。

3、创建urls.txt文件，内容是你要监控的网站，每行一个，英文逗号分隔，格式为：网站名称,截图名称,网址，例如：网易,wangyi,http://www.163.com ，可以用#开头取消监控。

4、执行python httpscreenshot.py，它每隔40秒会去扫一遍所有网站，生成新的截图。同时会自动生成一个新的index.html页面，可以根据这个页面中包含的更新时间判断脚本是否正常运行。只需用浏览器打开index.html一次，它也每隔40秒刷新一次，因此可以实现自动实时网页监控。

注：支持Docker部署，但是Docker环境下，脚本会因网络问题崩溃，原因不明，暂不能使用。
