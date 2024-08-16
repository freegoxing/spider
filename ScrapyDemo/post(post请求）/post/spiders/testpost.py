import scrapy
import json

class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["fanyi.baidu.com"]
    #post 请求若没有参数，就没意义
    #所以start_urls 没用
    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw' :'as'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)


    def parse_second(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)
















