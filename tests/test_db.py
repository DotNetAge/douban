# coding:utf-8
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from douban.modals import Book, db
from douban.items import BookItem
from douban.spiders import BookSpider
from .utils import mock_response
from scrapy.extensions.feedexport import IFeedStorage

class DataBaseTestCase(TestCase):

    def test_add_data(self):
        # 初始化数据库连接：
        engine = create_engine('sqlite:///test.db')
        db.metadata.bind = engine
        db.metadata.create_all()

        # 创建DBSession类型：
        DBSession = sessionmaker(bind=engine)

        session = DBSession()

        spider = BookSpider()
        item = spider.parse_item(mock_response("https://book.douban.com/tag", 'tests/data/book.html'))

        book = Book(**dict(item))
        session.add(book)
        session.commit()

        self.assertGreater(book.id, 0)

        session.close()
