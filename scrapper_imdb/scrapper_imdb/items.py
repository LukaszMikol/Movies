# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperImdbItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Year = scrapy.Field()
    Rating_value = scrapy.Field()
    Rating_count = scrapy.Field()
    Description = scrapy.Field()
    Director = scrapy.Field()
    Duration = scrapy.Field()
    Genre = scrapy.Field()
    Country = scrapy.Field()
    Language = scrapy.Field()
    Budget = scrapy.Field()
    Box_office_USA = scrapy.Field()
    Box_office_world = scrapy.Field()
    Url = scrapy.Field()