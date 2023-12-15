import scrapy


class PepParseItem(scrapy.Item):
    name = scrapy.Field()
    number = scrapy.Field()
    status = scrapy.Field()
