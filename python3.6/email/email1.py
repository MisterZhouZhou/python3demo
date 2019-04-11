#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "16619930394@163.com"  # 用户名
mail_pass = "zw16619930394"  # 口令

sender = '16619930394@163.com'
receivers = ['2861451012@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 邮件内容
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
# 标题
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')  # subject

try:
    smtpObj = smtplib.SMTP(mail_host)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)


# 发送一条简单邮件只包含文字