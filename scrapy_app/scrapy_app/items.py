# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuoteSpiderItem(scrapy.Item):
    text = scrapy.Field()  # The text of the quote
    author = scrapy.Field()  # The author of the quote
    tags = scrapy.Field()  # The tags associated with the quote
