from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy import Item
from scrapy import Field
import csv


import csv


class UrlItem(Item):
    url = Field()


class WikiSpider(CrawlSpider):
    allowed_domains = []
    start_urls = []
    name = 'news'
    
    with open('newssites.csv', newline='') as csvfile:

        linkreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(linkreader)

        for row in linkreader:
            start_urls.append(row[0])
            allowed_domains.append(row[1])
    

    rules = (
        Rule(LinkExtractor(), callback='parse_url'),
    )

    def parse_url(self, response):
        item = UrlItem()
        item['url'] = response.url

        return item