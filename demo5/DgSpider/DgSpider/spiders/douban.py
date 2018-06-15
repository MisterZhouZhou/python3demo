import scrapy
from scrapy.http import Request


class DoubanSpider(scrapy.Spider):
    name = "douban"  # 这个name是你必须给它一个唯一的名字  后面我们执行文件时的名字
    start_urls = ["https://movie.douban.com/top250"]
    # 这个列表中的url可以有多个，它会依次都执行，我们这里简单爬取一个
    url = "https://movie.douban.com/top250"
    # 因为豆瓣250有翻页操作，我们设置这个url用来翻页

    def parse(self, response):  # 默认函数parse
        sites = response.xpath(
            '//ol[@class="grid_view"]')  # <span style="font-family:Arial, Helvetica, sans-serif;">('匹配你所需信息的路径')</span>
        # xpath是scrapy里面的一种匹配方式，类似于正则表达式，还有其他几种匹配方式
        # 这里我们首先获得的是我们需要的信息的那一大块sites。

        print("！！！！！返回信息是：")
        info = sites.xpath('./li')
        # 从sites中我们再进一步获取到所有电影的所有信息
        for i in info:  # 这里的i是每一部电影的信息
            # 排名
            num = i.xpath('./div//em[@class=""]//text()').extract()  # 获取到的为列表类型
            # extract()是提取器  将我们匹配到的东西取出来
            print(num[0], end=";")
            # 标题
            title = i.xpath('.//span[@class="title"]/text()').extract()
            print(title[0], end=";")
            # 评论
            remark = i.xpath('.//span[@class="inq"]//text()').extract()
            # 分数
            score = i.xpath('./div//span[@class="rating_num"]//text()').extract()
            print(score[0])

        nextlink = response.xpath('//span[@class="next"]/link/@href').extract()
        # 还记得我们之前定义的url吗，由于电影太多网页有翻页显示，这里我们获取到翻页的那个按钮的连接nextlink
        if nextlink:  # 翻到最后一页是没有连接的，所以这里我们要判断一下
            nextlink = nextlink[0]
            print(nextlink)
            yield Request(self.url + nextlink, callback=self.parse)
            # yield中断返回下一页的连接到parse让它重新从下一页开始爬取，callback返回函数定义返回到哪里