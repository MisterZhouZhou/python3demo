# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-5-4 下午23:37
# @Author  : 杨星星
# @Email   : yangshilong_liu@163.com
# @File    : wechart.py
# @Software: PyCharm

# coding=utf8
import requests
import itchat
import random

# KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
# KEY = 'c3386bd8e60a434a8c5b5106dc766887'

KEY_LIST = ['8edce3ce905a4c1dbb965e6b35c3834d''c3386bd8e60a434a8c5b5106dc766887']


def get_response(msg):
    # 这里我们就是在调用别人的api接口 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': random.choice(KEY_LIST),
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return


# 这里用到的方法是通用的一个调用方法，具体的可以看下边的我粘贴来的用法详解
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    try:
        defaultReply = '我现在只想模仿你:' + msg['Text']
        # 在测试的发现他是无关政治，我想这句我要加上
        if '台湾' in msg['Text']:
            return '台湾是中国不可分割的一部分,支持祖国收复台湾,建立台湾省'
        # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text'])
        # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
        return reply or defaultReply
    except Exception as error:
        print(error)
        return


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
