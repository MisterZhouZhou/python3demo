from urllib import request
from bs4 import BeautifulSoup
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import collections
import matplotlib.pyplot as plt



def getHtml():
    url = r'http://www.tvzn.com/14784/yanyuanbiao.html'
    # 模拟真实浏览器进行访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read()
    page_info = page_info.decode('utf-8')

    return page_info

def getActorNames(contents1, contents2):
    actorNamesList = []
    for content in contents1:
        mainActorName = content.find("p", class_="mh-title").find("a", class_="mh-actor").string
        actorNamesList.append(mainActorName)

    for content in contents2:
        notMainActorName = content.find("p", class_="mh-l").find(class_="mh-actor").string
        actorNamesList.append(notMainActorName)
    return actorNamesList


def collectionNames(namelist):
    surnamelist = []
    givennamelist = []
    surname_dict = {}
    for actorname in nameList:
        surnamelist.append(actorname[0])
        for givenname in actorname[2:]:
            givennamelist.append(givenname)
        if actorname[0] not in surname_dict:
            surname_dict[actorname[0]] = 1
        else:
            surname_dict[actorname[0]] += 1
    return surnamelist, givennamelist, surname_dict


def wordCount(surenamelist):
    word_count = collections.Counter(surenamelist)
    backgroud_Image = plt.imread('test1.jpg')

    # 设置词云属性
    wc = WordCloud(font_path="/Users/zhouwei/Desktop/zw/python3/yanxidemo/simsun.ttc",  # 设置字体
                   background_color="white",  # 背景颜色
                   max_words=2000,  # 词云显示的最大词数
                   mask=backgroud_Image,  # 设置背景图片
                   max_font_size=100,  # 字体最大值
                   stopwords=STOPWORDS,
                   random_state=30,
                   width=1000, height=860)
    wc.generate_from_frequencies(word_count)
    img_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=img_colors)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    html = getHtml()
    # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
    soup = BeautifulSoup(html, 'html.parser')
    # 获取主演数据
    contents1 = soup.find('ul', class_="gclearfix").findAll("li")
    # 获取非主演数据
    contents2 = soup.find('ul', class_="glearfix").findAll("li")
    nameList = getActorNames(contents1, contents2)
    surnamelist, givennamelist, surname_dict = collectionNames(nameList)
    wordCount(surnamelist)