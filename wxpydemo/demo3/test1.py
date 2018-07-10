from wxpy import *

bot = Bot(cache_path=True, console_qr=True)
# 机器人账号自身
myself = bot.self
# 向文件传输助手发送消息
# bot.file_helper.send('Hello World!')

# 在 Web 微信中把自己加为好友
# error
# myself.add()
# myself.accept()
# myself.send('Hello World!')


minmin = ensure_one(bot.friends().search('小敏敏敏敏敏敏敏敏'))

@bot.register(minmin)
def forward_minmin_message(msg):
    msg.forward(bot.file_helper, prefix='敏敏发言')  #  forward(target)消息转发方法
    print(msg)



####################################################
# 记得加空格
feiniu = ensure_one(bot.groups().search('飞牛在天'))
# 定位王俊东
jundong = ensure_one(feiniu.search('王俊东北'))

@bot.register(feiniu)
def forward_feiniu_message(msg):
    print(msg,msg.member)
    if msg.member == jundong:
        return '{}傻帽发来消息: {}'.format(msg.member.name, msg.text)




####################################################
# file_helper = bot.file_helper
# @bot.register(file_helper)
# def forward_file_helper_message(msg):
#     print(msg.member)




####################################################
wanke = ensure_one(bot.groups().search('万科城丁晓娟5期 6期业主群'))

@bot.register(wanke)
def forward_wanke_message(msg):
    print(msg,msg.member.name)
    msg.forward(bot.file_helper, prefix='{}发来消息: {}'.format(msg.member.name, msg.text))




# 堵塞线程
embed()
