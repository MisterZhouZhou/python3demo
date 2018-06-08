# -*- coding: UTF-8 -*-

from urllib import request, error

if __name__ == '__main__':
    # 一个不存在的链接
    url = 'http://www.iloveyou.com/'
    response = request.urlopen(url)
    try:
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError")
            print('===>',e.code)
        elif hasattr(e, 'reason'):
            print("URLError")
            print('++++>>>',e.reason)