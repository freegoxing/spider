import scrapy
from dang.items import DangItem



class DSpider(scrapy.Spider):
    name = "d"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        print('==============')
        # src_list = response.xpath('//ul[@class="bigimg"]//img/@data-original').extract()
        # name_list = response.xpath('//ul[@class="bigimg"]/li/a/@title').extract()
        # price_list = response.xpath('//ul[@class="bigimg"]/li/p[@class="price"]/span[@class="search_now_price"]/text()').extract()
        # for i in range(len(src_list)):
        #     src = src_list[i]
        #     name = name_list[i+1]
        #     price = price_list[i+1]
        #     print(src, name, price)

        li_list = response.xpath('//ul[@class="bigimg"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()
            # print(src, name, price)

            book = DangItem(src=src, name=name, price=price)
            # 获取一个就利用book交给pipelines
            yield book
        print('='*50)


        if self.page <2:
            self.page += 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
            yield scrapy.Request(url=url, callback=self.parse)


