# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    #访问网址, 该网址会返回你的IP
    url = 'http://www.baidu.com/'
    #这是代理IP
    proxy = {'http':'171.37.166.199:8123'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)


    # 报错，无法正常运行