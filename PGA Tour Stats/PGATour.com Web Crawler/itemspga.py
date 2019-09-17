import scrapy

class GolfItem(scrapy.Item):
    PlayerName = scrapy.Field()
    Statistic = scrapy.Field()
    Variable = scrapy.Field()
    Value = scrapy.Field()
    Date = scrapy.Field()

    