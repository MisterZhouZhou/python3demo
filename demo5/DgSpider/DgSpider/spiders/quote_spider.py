import scrapy
from DgSpider.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
    ]
    # 此时只是将页面代码下载下来并保存，没有进行分析
    def parse(self, response):
        print('========================')
        # 爬取所需内容
        for quote in response.xpath('//div[@class="quote"]'):
            item = QuoteItem()
            item['text'] = quote.xpath('span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('span/small/text()').extract_first()
            yield item
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # 如果找得到下一页的连接，创建一个request并且设定这个request的callback为parse（）
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

