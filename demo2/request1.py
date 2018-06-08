# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen('http://fanyi.baidu.com')
    html = response.read()
    # html = html.decode("utf-8")
    # 获取编码类型
    charset = chardet.detect(html)
    print(charset)
    html = html.decode(charset['encoding'])
    print(html)
