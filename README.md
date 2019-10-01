# httpscreenshot

1、创建urls.txt文件，内容是你要监控的网站，每行一个，英文逗号分隔，格式为：网站名称,截图名称,网址，例如：网易,wangyi,http://www.163.com ，可以用#开头取消监控。

2、执行python httpscreenshot.py。

3、支持Docker部署，但是Docker环境下，脚本会因网络问题崩溃，原因不明。
