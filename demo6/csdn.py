#!usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017年3月19日
@author: SUN HuaQiang
目的：使用python爬取csdn个人博客的访问量，主要用来练手Python爬虫
收获：1.了解Python爬虫的基本过程
      2.在Python2的基础上实现Python3,通过对比发现版本之间的差异
'''

import urllib.request
import urllib
import re

# 当前博客列表页号
page_num = 1
# 初始化最后列表的页码
notLast = 1

account = str(input('请输入csdn的登录账号:'))
while notLast:
    # 首页地址
    baseUrl = 'http://blog.csdn.net/' + account
    # 连接页号，组成爬取的页面网址
    myUrl = baseUrl + '/article/list/' + str(page_num)
    # 伪装成浏览器访问，直接访问的话csdn会拒绝
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    # 构造请求
    req = urllib.request.Request(myUrl, headers=headers)
    # 访问页面
    myResponse = urllib.request.urlopen(req)
    # python3中urllib.read返回的是bytes对象，不是string,得把它转换成string对象，用bytes.decode方法
    myPage = myResponse.read().decode()
    # 在页面中查找是否存在‘尾页'这一个标签来判断是否为最后一页
    notLast = re.findall('<a href=".*?">尾页</a>', myPage, re.S)
    print('-----------第%d页--------------' % (page_num,))
    # 利用正则表达式来获取博客的标题
    title = re.findall('<span class="link_title"><a href=".*?">(.*?)</a></span>', myPage, re.S)
    titleList = []
    for items in title:
        titleList.append(str(items).lstrip().rstrip())
    # 利用正则表达式获取博客的访问量
    view = re.findall('<span class="link_view".*?><a href=".*?" title="阅读次数">阅读</a>\((.*?)\)</span>', myPage, re.S)
    viewList = []
    for items in view:
        viewList.append(str(items).lstrip().rstrip())
    # 将结果输出
    for n in range(len(titleList)):
        print('访问量:%s 标题:%s' % (viewList[n].zfill(4), titleList[n]))
    # 页号加1
    page_num = page_num + 1