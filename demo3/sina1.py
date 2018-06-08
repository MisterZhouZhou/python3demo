# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import json
import pandas
import sqlite3

sinaNewsURL = 'http://news.sina.com.cn/china'
commonPage = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}'

# 获取分页新闻数据
def getNewLists(commonPage):
    newsList = []
    for i in range(1,2):
        newsPage = commonPage.format(i)
        reContent = requests.get(newsPage)
        reContent.encoding = 'utf-8'
        if reContent.status_code == 200:
            jsonData = json.loads(reContent.text)
            for newDic in jsonData['result']['data']:
                newsURL = newDic['url']
                newsList.append(getNewsDetail(newsURL))
        else:
            print('分页结束******')
            break

        return newsList


#1- 获取china首页新闻列表（后面用不到, 可以用这个拿到新闻链接, 然后再测试新闻详情函数）
def getNewsListData(newsURl):
    newsList = []
    reContent = requests.get(newsURl)
    reContent.encoding = 'utf-8'
    soupContent = BeautifulSoup(reContent.text, 'html.parser')
    newsSoupList = soupContent.select('.news-item')
    for newsSoup in newsSoupList:
        newsModel = {}
        if len(newsSoup.select('h2')) > 0:
            news = newsSoup.select('h2')[0]
            newsTime = newsSoup.select('.time')[0]

            # 获取href
            a = news.select('a')[0]
            href = a['href']
            # 获取新闻ID
            m = re.search('doc-i(.*?).shtml', href)
            newsID = m.groups(1)

            # 获取title
            title = news.text

            # 获取时间
            time = newsTime.text
            newsModel['newsID'] = newsID
            newsModel['newsHref'] = href
            newsModel['title'] = title
            newsModel['time'] = time

            newsList.append(newsModel)
    return newsList

# 获取新闻内容详情
def getNewsDetail(newsUrl):
    newsModel = {}
    reContetn = requests.get(newsUrl)
    reContetn.encoding = 'utf-8'
    soupContent = BeautifulSoup(reContetn.text, 'html.parser')
    # print(soupContent)
    # 获取新闻id
    match = re.search('doc-i(.*?).shtml', newsUrl)
    newsID = match.groups(1)[0]
    # print('===',match.groups(1)[0])
    # 获取新闻标题
    title = soupContent.select('.main-title')[0].text
    # 获取时间
    time = soupContent.select('.date-source span')[0].text
    # 获取来源
    source = ''
    if len(soupContent.select('.date-source a')) > 0:
        source = soupContent.select('.date-source a')[0].text
        # print(source)
    elif len(soupContent.select('.source')) > 0:
        source = soupContent.select('.source')[0].text

    else:
        print('当前未检测到来源', newsUrl)

    # 获取内容
    article = ''.join([article.text.strip() for article in soupContent.select('.article p')])
    # 获取编辑/作者
    show_author = soupContent.select('.show_author')[0].text
    newsModel['newsID'] = newsID
    newsModel['newsHref'] = newsUrl
    newsModel['title'] = title
    newsModel['time'] = time
    newsModel['source'] = source
    newsModel['article'] = article
    newsModel['show_author'] = show_author
    return newsModel





if __name__ == '__main__':
   # print(getNewsListData(sinaNewsURL))
   #  newsList = getNewsListData(sinaNewsURL)
   #  newModel = newsList[0]
   #  newsDetailModel = getNewsDetail(newModel['newsHref'])
   #  print(newsDetailModel)

   newsList= getNewLists(commonPage)
   print(newsList)
   # 保存数据
   df = pandas.DataFrame(newsList)
   # df.to_excel('news.xlsx')

   # 新建数据库news.sqlite  创建并保存至news表
   with sqlite3.connect('news.sqlite') as db:
       df.to_sql('news', con=db)


   with sqlite3.connect('news.sqlite') as db:
       df3 = pandas.read_sql_query('SELECT * FROM news', con=db)
       print('查找数据库:********', df3.head(1))

   # df2 = pandas.DataFrame([{'name': 'zw', 'age': 10}])
   # with sqlite3.connect('newss.sqlite') as db:
   #     df2.to_sql('newss', con=db)

   # with sqlite3.connect('newss.sqlite') as db:
   #     df3 = pandas.read_sql_query('SELECT * FROM newss', con=db)
   #     print('查找数据库:********', df3.head(1))