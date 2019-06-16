# coding:utf-8
from redis import Redis


redis = Redis(host='127.0.0.1', port=6379, db=0)

# 写入Redis启动分布式爬虫网络
redis.lpush('spider:start_urls', 'https://book.douban.com/tag/')