# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymysql


class JobAnalysisPipeline(object):
    def process_item(self, item, spider):
        sql='''
        insert into jobdata(
        address,
        company,
        education,
        experiment,
        industry,
        salary,
        size,
        title
                )
                VALUES
                (
               '%s','%s','%s','%s','%s','%s','%s','%s'
                )
        '''%(item["address"],item['company'],item['education'],item['experiment'],item['industry'],item['salary'],item['size'],item['title'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def __init__(self):
        self.conn=pymysql.connect(host="localhost",user='root',password='12345678',database='job',charset='utf8')
        self.cursor=self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
