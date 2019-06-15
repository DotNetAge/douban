# -*- coding: utf-8 -*-

# Scrapy settings for douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanbook'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7',

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

FEED_FORMAT = 'entity'  # 数据导出的格式
FEED_EXPORTERS = {  # 关联导出格式与数据项导出器
    'entity': 'douban.extensions.SQLItemExporter'
}

FEED_URI = 'sqlite:///test.db'  # 数据库的连接字符串

# 增加对sqlite，postgresql和mysql内种协议的存储端支持
FEED_STORAGES = {
    'sqlite': 'douban.extensions.SQLFeedStorage',
    'postgresql': 'douban.extensions.SQLFeedStorage',
    'mysql': 'douban.extensions.SQLFeedStorage'
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'douban.middlewares.RandomProxyMiddleware': 501,
    'douban.middlewares.RandomUserAgentMiddleware': 800
}

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'
]

HTTP_PROXIES = [

]

COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

AUTOTHROTTLE_ENABLED = True  # 一定要打开，否则自动降速就会禁用
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
