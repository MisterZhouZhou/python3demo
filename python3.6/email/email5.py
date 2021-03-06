import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "16619930394@163.com"  # 用户名
mail_pass = "zw16619930394"  # 授权密码，非登录密码

receivers = ['2861451012@qq.com','1984774346@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 邮件主题
title = '人生苦短'
# 邮件内容
content  = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""

# 邮件格式处理
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(title, 'utf-8')  # subject
msg['From']= formataddr(["周巍", mail_user])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
# msg['To'] = formataddr(["FK", ','.join(receivers)])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
# 多人邮件加上面的就报错
msg['To'] = ','.join(receivers)

def send_email_SMTP(SMTP_host, from_account, from_passwd, to_account, msg):
    try:
        email_client = smtplib.SMTP(SMTP_host)
        email_client.login(from_account, from_passwd)
        email_client.sendmail(from_account, to_account, msg.as_string())
        email_client.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    receiver = receivers
    send_email_SMTP(mail_host, mail_user, mail_pass, receiver, msg)

# 成功
# 发送一条链接，发件人昵称, 发多人邮件