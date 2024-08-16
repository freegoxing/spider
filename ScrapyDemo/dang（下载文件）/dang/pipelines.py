# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DangPipeline:
    def open_spider(self, spider):
        print('+'*50)
        self.fp = open('book.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item


    def close_spider(self, spider):
        self.fp.close()
        print('+'*50)


import urllib.request
#d多条管道下载
class DangDownLoadPipeline:
    def process_item(self, item, spider):

        src = 'http:' + item.get('src')
        # filename = 'D:\coding\python\python.project.pycharm\pythonProject\study_spiders\ScrapyDemo\dang\dang\spiders\books' + item.get('name') +'.jpg'
        filename = item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=src, filename=filename)

        return item