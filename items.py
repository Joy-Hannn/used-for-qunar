# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class  gongsiItem(scrapy.Item):
    name = scrapy.Field()       # 公司名称
    url = scrapy.Field()        # 公司对应url
