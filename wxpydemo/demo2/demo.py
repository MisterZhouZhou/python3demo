from wxpy import  *
from pyecharts import Pie,Map
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as Image


# web微信登录
def login():
    # 初始化机器人，扫码登录
    bot = Bot()
    # 获取所有好友
    my_friends = bot.friends()
    return my_friends


# 显示性别比例
def show_sex_ratio(friends):
    male = female = other = 0
    for friend in friends:
        sex = friend.sex
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1

    # 统计总数，抛出自己
    total = len(friends[1:])

    # 对好友数据进行分析
    attr = ['男性', '女性', '其他']
    v1 = [float(male), float(female), float(other)]
    pie = Pie('饼图-环形图示例', title_pos='center')
    pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient='vertical',
            legend_pos='left')
    pie.render("sex.html")


def show_area_distribution(friends):
    # 因为获取的列表城市都没有带市字，而pyecharts需要带个市字
    b = '市'
    def s(x):
        return x + b

    # 因为我好友里面除了广东的外和其他的，剩下非广东的寥寥无几，所以只提取广东的
    bot = Bot(cache_path=True)
    friends = friends.search(province='广东')
    citys = []
    for friend in friends:
        city = friend.city
        citys.append(city)
    print(citys)
    # r = map(s, citys)
    # cityss = list(r)
    cityss = citys

    # 为城市计数
    a = {}
    for i in cityss:
        a[i] = cityss.count(i)
    # a.pop('市')

    # 把字典进行有序拆分为2个列表
    attrs = []
    values = []
    for value, attr in a.items():
        values.append(attr)
        attrs.append(value)
    # 开始绘图
    map = Map("广东地图示例", width=1200, height=600)
    map.add("", attrs, values, maptype='广东', is_visualmap=True, visual_text_color='#000')
    map.render("city.html")

# 好友签名
def show_signature(friends):
    male = female = other = 0

    # 提取好友签名，并去掉span，class，emoji，emoji1f3c3等的字段
    signatures = []
    for i in friends:
        signature = i.signature.strip().replace("span", "").replace("class", "").replace("emoji", "")
        # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
        rep = re.compile("1f\d.+")
        signature = rep.sub("", signature)
        signatures.append(signature)
    # 拼接字符串
    text = "".join(signatures)
    # jieba分词
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_jieba)

    # wordcloud词云
    my_wordcloud = WordCloud(background_color="white",
                             max_words=2000,
                             max_font_size=1000,
                             random_state=42,# 使用font的绝对路径
                             font_path='/Users/zhouwei/Desktop/python/python3demo/wxpydemo/demo2/hanyi.ttf').generate(wl_space_split)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()



def main():
    friends = login()
    show_sex_ratio(friends)
    show_area_distribution(friends)
    show_signature(friends)

if __name__ == '__main__':
    main()