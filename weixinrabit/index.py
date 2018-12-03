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
import os

# KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
# KEY = 'c3386bd8e60a434a8c5b5106dc766887'
# f67c9021fdf3406fa29f9f4d4aff6ae0
KEY_LIST = ['f67c9021fdf3406fa29f9f4d4aff6ae0']


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
        r = requests.post(apiUrl, data=data).json() # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        if(r.get('code') == 200000):  # 图片搜索
           return image_search(r)
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return


# 图片搜索
def image_search(dict):
    return dict['text']+'  '+dict['url']

# 监听文本消息
@itchat.msg_register(itchat.content.TEXT)
def tuling_replay(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    try:
        defaultReply = '我现在只想模仿你:' + msg['Text']
        # 在测试的发现他是无关政治，我想这句我要加上
        if '台湾' in msg['Text']:
            return '台湾是中国不可分割的一部分,支持祖国收复台湾,建立台湾省'

        reply = get_response(msg['Text'])
        return reply or defaultReply
    except Exception as error:
        print(error)
        return


# 监听图片消息
@itchat.msg_register(itchat.content.PICTURE)
def image_replay(msg):
    try:
        defaultReplay = 'I love picture'
        # 以下方法会下载文件
        path = './images/'   # 图片路径
        dirs = os.listdir(path)
        # 保存的会有一样的图片。。。
        #msg['Text'](path+msg['FileName'])
        reply = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), path+random.choice(dirs))
        return reply or defaultReplay
    except Exception as error:
        return


# 收到好友邀请自动添加好友
@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you ^_^', msg['RecommendInfo']['UserName'])


# 监听小组文本消息
@itchat.msg_register([itchat.content.TEXT, itchat.content.PICTURE], isGroupChat=True)
def group_replay(msg):
    # 判断是否有人@自己
    if msg['isAt']:
        reply = get_response(msg['Text'])
        if reply == '请按规定的要求进行加密':  # 机器人开启密钥后会一直提示这句话
            return "嘤嘤嘤，吓到人家了，不能对宝宝温柔点么。"
        else:
            return reply
    if(msg['Type'] == 'Picture'):
        path = './images/'  # 图片路径
        dirs = os.listdir(path)
        reply = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), path + random.choice(dirs))
        return reply
    try:
        defaultReply = '我现在只想模仿你:' + msg['Text']
        # 在测试的发现他是无关政治，我想这句我要加上
        if '台湾' in msg['Text']:
            return '台湾是中国不可分割的一部分,支持祖国收复台湾,建立台湾省'

        reply = get_response(msg['Text'])
        return reply or defaultReply
    except Exception as error:
        print(error)
        return


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
