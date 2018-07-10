
# -*- coding: utf-8 -*-
from qqbot import QQBotSlot as qqbotslot, RunBot, _bot as bot

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if '周巍' == member.name:
        bot.SendTo(contact, '打你哦')
        return
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '在':
        bot.SendTo(contact, '我一直在呢，嘻嘻')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()


def main(bot):
    # bot.SendTo('2861451012','dd')
    friends = bot.List('buddy')
    groups = bot.List('group')
    # print(friends)
    # print('-========')
    # print(groups)
    zhouwei = bot.List('buddy', '周巍')
    if zhouwei:
        zw = zhouwei[0]
        bot.SendTo(zw, 'hello')


if __name__ == '__main__':
    # bot.Login(['-q', '1984774346'])
    # main(bot)
    RunBot()