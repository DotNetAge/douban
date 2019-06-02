# coding:utf-8
import unittest
import os
import re
from douban.spiders.book import BookSpider
from scrapy.http import HtmlResponse, Request


class SpiderTest(unittest.TestCase):

    def mock_response(self, target_url, mock_file):
        with open(mock_file, 'r') as tag_file:
            body = tag_file.read()

        return HtmlResponse(url=target_url,
                            request=Request(target_url),
                            body=body, encoding="utf-8")

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
            [self.assertIsNotNone(check_result(r)) for r in spider.parse(self.mock_response(*kv))]

    def test_parse_item(self):
        spider = BookSpider()
        item = spider.parse_item(self.mock_response("https://book.douban.com/tag", 'tests/data/book.html'))
        self.assertEqual(item['name'], u'解忧杂货店')
        self.assertEqual(item['authors'], u'[日]东野圭吾')
        self.assertEqual(item['publishing_house'], u'南海出版公司')
        self.assertEqual(item['publisher'], u'新经典文化')
        self.assertEqual(item['origin_name'], u'ナミヤ雑貨店の奇蹟')
        self.assertEqual(item['translators'], u'李盈春')
        self.assertEqual(item['pub_date'], u'2014-05-02T00:00:00')
        self.assertEqual(item['pages'], u'291')
        self.assertEqual(item['price'], u'39.50')
        self.assertEqual(item['isbn'], u'9787544270878')
        self.assertEqual(item['rates'], u'8.5')
        self.assertEqual(item['rating_count'], u'438151')
        self.assertIsNotNone(item['summary'])
