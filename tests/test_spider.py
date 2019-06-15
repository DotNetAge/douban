# coding:utf-8
import unittest
import re
from douban.spiders.book import BookSpider
from .utils import mock_response

class SpiderTest(unittest.TestCase):


    def test_crawl_rules(self):
        spider = BookSpider()
        spider._follow_links = True
        url_and_files = [
            ("https://book.douban.com/tag", 'tests/data/tag.html'),
            ("https://book.douban.com/tag", 'tests/data/tag_list.html'),
            ("https://book.douban.com/tag", 'tests/data/book.html')
        ]

        def check_result(request):
            return re.search(u'\/tag\/(.*?)\?start\=', request.url) is not None or \
                   re.search(u'\/tag\/(.*?)', request.url) is not None or \
                   re.search(u'\/subject\/.*', request.url) is not None

        for kv in url_and_files:
            [self.assertIsNotNone(check_result(r)) for r in spider.parse(mock_response(*kv))]

    def test_parse_item(self):
        spider = BookSpider()
        item = spider.parse_item(mock_response("https://book.douban.com/tag", 'tests/data/book.html'))
        self.assertEqual(item['name'], u'解忧杂货店')
        self.assertEqual(item['authors'], u'[日]东野圭吾')
        self.assertEqual(item['publishing_house'], u'南海出版公司')
        self.assertEqual(item['publisher'], u'新经典文化')
        self.assertEqual(item['origin_name'], u'ナミヤ雑貨店の奇蹟')
        self.assertEqual(item['translators'], u'李盈春')
        # self.assertEqual(item['pub_date'], u'2014-05-15T00:00:00')
        self.assertEqual(item['pages'], 291)
        self.assertEqual(item['price'], 39.5)
        self.assertEqual(item['isbn'], u'9787544270878')
        self.assertEqual(item['rates'], 8.5)
        self.assertEqual(item['rating_count'],438151)
        self.assertIsNotNone(item['summary'])
