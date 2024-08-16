# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DushuwangPipeline:
    def open_spider(self, spider):
        self.fp = open('dushuwang.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item


    def close_spider(self, spider):
        self.fp.close()
#加载settings文件
from scrapy.utils.project import get_project_settings
import pymysql

class MysqlPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        # DB_HOST = 'localhost'
        # DB_PORT = 3306
        # DB_NAME = 'spider1'
        # DB_USER = 'root'
        # DB_PASSWORD = 'qwer1234QWER'
        # DB_CHARSET = 'utf8'
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.name = settings['DB_NAME']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            db=self.name,
            charset=self.charset,
            password=self.password
        )

        self.corsor = self.conn.cursor()


    def process_item(self, item, spider):

        sql = 'insert into book(name, url) values("{}", "{}")'.format(item['name'], item['url'])
        self.corsor.execute(sql)
        self.conn.commit()

        return item


    def close_spider(self, spider):
        self.corsor.close()
        self.conn.close()
