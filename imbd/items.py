# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImbdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    ratings = scrapy.Field()
    others = scrapy.Field()
    duration = scrapy.Field()
    plot = scrapy.Field()
    Playing_as = scrapy.Field()
    director  = scrapy.Field()
    writer = scrapy.Field()

    
    
