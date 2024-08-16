import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dushuwang.items import DushuwangItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1002.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/\d+.html"),
                                callback="parse_item",
                                follow=True),
             )

    def parse_item(self, response):

        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@alt').extract_first()
            url = img.xpath('./@data-original').extract_first()
            print(name, url)

            book = DushuwangItem(name=name, url=url)
            yield book


