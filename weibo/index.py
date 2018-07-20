# 导入相关库
import requests
import json
import time
import pandas as pd
# import fool
from PIL import Image,ImageSequence
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt


# 获取微博ID
def getWeibo_id():
    content_parameter = []  # 用来存放weibo_id值
    # 获取每条微博的id值
    url = 'https://m.weibo.cn/api/container/getIndex?uid=1773294041&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%8E%8B%E8%8F%8A&\featurecode=20000320&type=uid&value=1773294041&containerid=1076031773294041'

    c_r = requests.get(url)
    for i in range(2, 11):
        c_parameter = (json.loads(c_r.text))['data']['cards'][i]['mblog']['id']
        content_parameter.append(c_parameter)
    return content_parameter

# 获取微博评论url
def getWeibo_comment_url(content_parameter):
    comment_url = []  # 用来存放weibo_url
    # 获取每条微博评论url
    c_url_base = 'https://m.weibo.cn/api/comments/show?id='
    for parameter in content_parameter:
        #  101
        for page in range(1, 3):  # 提前知道每条微博只可抓取前100页评论
            c_url = c_url_base + str(parameter) + '&page=' + str(page)
            comment_url.append(c_url)
    return comment_url


# 获取user_id和comment
def getWeibo_user_idAndComment(comment_url):
    # 获取每个user_id和comment
    user_id = []  # 用来存放user_id
    comment = []  # 用来存放comment
    for url in comment_url:
        u_c_r = requests.get(url)
        try:
            for m in range(0, 9):  # 提前知道每个url会包含9条用户信息
                one_id = json.loads(u_c_r.text)["data"]["data"][m]["user"]["id"]
                user_id.append(one_id)
                one_comment = json.loads(u_c_r.text)["data"]["data"][m]["text"]
                comment.append(one_comment)
        except:
            pass
    return user_id,comment


# 获取用户containerid
def getUserContainerid(user_id):
    containerid = []
    user_base_url = "https://m.weibo.cn/api/container/getIndex?type=uid&value="
    for id in set(user_id):  # 需要对user_id去重
        containerid_url = user_base_url + str(id)
        try:
            con_r = requests.get(containerid_url)
            one_containerid = json.loads(con_r.text)["data"]['tabsInfo']['tabs'][0]["containerid"]
            containerid.append(one_containerid)
        except:
            containerid.append(0)
    return containerid

# 获取用户基本信息
def getUserInfo(user_id,containerid):
    # 这里需要设置headers以及cookie模拟登陆
    feature = []  # 存放用户基本信息
    comment = []  # 评论内容
    id_lose = []  # 存放请求失败id
    user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36"
    headers = {"User-Agent": user_agent}
    m = 1
    for num in zip(user_id, containerid):
        # url = "https://m.weibo.cn/api/container/getIndex?uid=" + str(
        #     num[0]) + "&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value=" + str(
        #     num[0]) + "&containerid=" + str(num[1])
        # https://m.weibo.cn/api/container/getIndex?containerid=2302831662434310_-_INFO&luicode=10000011&lfid=2302831662434310&featurecode=20000320
        url = "https://m.weibo.cn/api/container/getIndex?containerid=" + str(num[1]) + "_-_INFO&luicode=10000011&lfid=2302831662434310&featurecode=20000320"
        print(url)
        try:
            # r = requests.get(url, headers=headers, cookies=cookie)
            r = requests.get(url, headers=headers, cookies=None)
            feature.append([json.loads(r.text)["data"]["cards"][1]["card_group"][1]["item_content"], "999岁", '未知', json.loads(r.text)["data"]["cards"][1]["card_group"][2]["item_content"]])
            # feature.append("999岁")
            # feature.append('未知')
            # feature.append(json.loads(r.text)["data"]["cards"][1]["card_group"][2]["item_content"])
            comment.append()
            print("成功第{}条".format(m))
            m = m + 1
            time.sleep(1)  # 设置睡眠一秒钟，防止被封
        except:
            id_lose.append(num[0])

    # 将featrue建立成DataFrame结构便于后续分析
    print('=====',feature)
    user_info = pd.DataFrame(feature, columns=["性别", "年龄", "星座", "国家城市"])
    user_info.to_csv('user_infos.csv', index=False)
    print('已保存为csv文件.')
    return user_info


# 获取评论信息
def getCommnetInfo(user_id,containerid):
    # 这里需要设置headers以及cookie模拟登陆
    feature = []  # 存放用户基本信息
    comment = []  # 评论内容
    id_lose = []  # 存放请求失败id
    user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36"
    headers = {"User-Agent": user_agent}
    m = 1
    for num in zip(user_id, containerid):
        url = "https://m.weibo.cn/api/container/getIndex?uid=" + str(
            num[0]) + "&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value=" + str(
            num[0]) + "&containerid=" + str(num[1])
        # https://m.weibo.cn/api/container/getIndex?containerid=2302831662434310_-_INFO&luicode=10000011&lfid=2302831662434310&featurecode=20000320
        url = "https://m.weibo.cn/api/container/getIndex?containerid=2302835260696504_-_INFO&luicode=10000011&lfid=2302831662434310&featurecode=20000320"
        print(url)
        try:
            # r = requests.get(url, headers=headers, cookies=cookie)
            r = requests.get(url, headers=headers, cookies=None)
            feature.append([json.loads(r.text)["data"]["cards"][1]["card_group"][1]["item_content"], "999岁", '未知', json.loads(r.text)["data"]["cards"][1]["card_group"][2]["item_content"]])
            # feature.append("999岁")
            # feature.append('未知')
            # feature.append(json.loads(r.text)["data"]["cards"][1]["card_group"][2]["item_content"])
            comment.append()
            print("成功第{}条".format(m))
            m = m + 1
            time.sleep(1)  # 设置睡眠一秒钟，防止被封
        except:
            id_lose.append(num[0])

    # 将featrue建立成DataFrame结构便于后续分析
    print('=====',feature)
    user_info = pd.DataFrame(feature, columns=["性别", "年龄", "星座", "国家城市"])
    user_info.to_csv('user_infos.csv', index=False)
    print('已保存为csv文件.')
    return user_info

# 进行分词
def fenci():
    # comment_data = pd.read_csv(r"comment.csv", encoding='GB18030')
    # 处理完以后再次载入进来
    comment_data = pd.read_excel(r"comment.xlsx", header=None)
    # 将数据转换成字符串
    # text = (",").join(comment_data)
    # 进行分词
    # cut_text = ' '.join(fool.cut(text))

    image = Image.open('background.jpeg')  # 作为背景形状的图
    graph = np.array(image)
    # 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
    wc = WordCloud(font_path="/Users/zhouwei/Desktop/python/python3demo/weibo/hanyi.ttf", background_color='White', max_words=150, mask=graph)

    name = ["女性", "摩羯座", "20岁", "21岁", "22岁", "23岁", "24岁", "25岁", "广州", "杭州", "成都", "武汉", "长沙", "上海", "北京", "海外", "美国",
            "深圳"]
    value = [20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # 词的频率
    dic = dict(zip(name, value))  # 词频以字典形式存储
    wc.generate_from_frequencies(dic)  # 根据给定词频生成词云
    image_color = ImageColorGenerator(graph)
    plt.imshow(wc)
    plt.axis("off")  # 不显示坐标轴
    plt.show()
    wc.to_file('wordcloud.jpg')

    print(comment_data.to_string)

def main():
    print('开始抓取weiboID...')
    content_parameter = getWeibo_id()
    print('开始抓取评论url...')
    comment_url = getWeibo_comment_url(content_parameter)
    print('开始抓取评论userid和comment...')
    user_id,comment = getWeibo_user_idAndComment(comment_url)
    pd.DataFrame(comment).to_csv(r"comment.csv", encoding='GB18030')
    print('评论内容保存成功')
    print('开始抓取评论用户containerid...')
    # containerid = getUserContainerid(user_id)
    # print('开始抓取评论用户信息...')
    # user_infos = getUserInfo(user_id,containerid)
    # print('开始抓取评论内容')



if __name__ == '__main__':
    # main()
    fenci()