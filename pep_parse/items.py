import scrapy


class PepItem(scrapy.Item):
    number = scrapy.Field()
    author = scrapy.Field()
    status = scrapy.Field()


class PepParseItem(scrapy.Item):
    pass
