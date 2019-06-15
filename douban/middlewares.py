# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


import random

class RandomUserAgentMiddleware(object):
    """
    随机User Agent 中间件
    """
    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agents=crawler.settings.getlist('USER_AGENTS'))

    def __init__(self, user_agents=[]):
        self.user_agents = user_agents

    def process_request(self, request, spider):
        if self.user_agents != None and len(self.user_agents) > 0:
            request.headers.setdefault(
                b'User-Agent', random.choice(self.user_agents))



class RandomProxyMiddleware(object):
    """
    随机代理。在运行时会从settings.py设置的PROXIES中随机抽取一个作为当前代理地址。
    """
    @classmethod
    def from_crawler(cls, crawler):
        return cls(proxies=crawler.settings.getlist('HTTP_PROXIES'))

    def __init__(self, proxies=[]):
        self.proxies = proxies

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxies)