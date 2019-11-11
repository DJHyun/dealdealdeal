# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import unicode_literals
import json
import codecs

from twisted.enterprise import adbapi
import datetime
import logging
import MySQLdb.cursors
from scrapy.exceptions import DropItem
from crawler.items import Hotdeal
import sys
import hashlib
from scrapy.http import Request
from sqlalchemy.orm import sessionmaker
from crawler.models import HotdealDB, db_connect, create_table


# class CrawlerPipeline(object):
    # json파일로 저장할때
    # def __init__(self):
    #     self.file = codecs.open("Hotdeal.json",'w',encoding='utf-8')#크롤링할 데이터를 저장할 파일 open

    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item),ensure_ascii=False) + "\n"
    #     self.file.write(line) #파일에 기록
    #     return item

    # def spider_closed(self,spider):
    #     self.file.close()


class CrawlerPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        # print("DB입력시작")
        session = self.Session()
        is_rear = session.query(HotdealDB).filter_by(title=item["title"],link=item["link"],time=item["time"]).first()
        if is_rear :#기존에 저장된 DB에 있으면 pass
            return item
        else:#기존에 저장된 DB에 없으면 insert후 commit
            hotdealdb = HotdealDB()
            hotdealdb.title = item["title"]
            hotdealdb.link = item["link"]
            hotdealdb.time = item["time"]
            try:
                session.add(hotdealdb)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
        # print("DB입력끝")
        return item
