# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen('http://fanyi.baidu.com')
    print("geturl打印信息：%s" % (response.geturl()))
    print('**********************************************')
    print("info打印信息：%s" % (response.info()))
    print('**********************************************')
    print("getcode打印信息：%s" % (response.getcode()))
    # html = html.decode("utf-8")
    html = response.read()
    # 获取编码类型
    charset = chardet.detect(html)
    print(charset)
    html = html.decode(charset['encoding'])
    print(html)
