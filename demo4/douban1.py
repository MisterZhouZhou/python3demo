# -*- coding: UTF-8 -*-

import scrapy
from scrapy.http import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/top250']
    url = 'https://movie.douban.com/top250'
    def parse(self, response):
        sites = response.xpath('//ol[@class="grid_view"]')
        info = sites.xpath('./li');
        for i in info:
            num = i.xpath('./div//em[@class=""]//text()').extract()
            title = i.xpath('.//span[@class="title"]/text()').extract()
            remark = i.xpath('.//span[@class="inq"]//text()').extract()
            # 分数
            score = i.xpath('./div//span[@class="rating_num"]//text()').extract()
        nextlink = response.xpath('//span[@class="next"]/link/@href').extract()
        if nextlink:  # 翻到最后一页是没有连接的，所以这里我们要判断一下
            nextlink = nextlink[0]
            print(nextlink)
            yield Request(self.url + nextlink, callback=self.parse)
