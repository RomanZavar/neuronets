# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DromparserItem(scrapy.ScrapyItem):
    # define the fields for your item here like:
    name = scrapy.Field()
    yers = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
