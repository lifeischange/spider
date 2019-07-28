# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobAnalysisItem(scrapy.Item):
    #name = scrapy.Field()
    title=scrapy.Field()
    salary=scrapy.Field()
    address=scrapy.Field()
    experiment=scrapy.Field()
    education=scrapy.Field()
    industry=scrapy.Field()
    company=scrapy.Field()
    size=scrapy.Field()
