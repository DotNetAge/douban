from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime

# 创建对象的基类：
db = declarative_base()


class Book(db):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    # 书名
    name = Column(String(255))
    # 作者
    authors = Column(String(255))
    # 出版社
    publishing_house = Column(String(255))
    # 出品方
    publisher = Column(String(255))
    # 原名
    origin_name = Column(String(255))
    # 译者
    translators = Column(String(255))
    # 出版时间
    pub_date = Column(DateTime())
    # 页数
    pages = Column(Integer())
    # 定价
    price = Column(Float())
    # ISBN
    isbn = Column(String(255))
    # 豆瓣评分
    rates = Column(Float())
    # 评价数
    rating_count = Column(Integer())
    summary = Column(Text)
    # 作者简介
    about_authors = Column(Text)
