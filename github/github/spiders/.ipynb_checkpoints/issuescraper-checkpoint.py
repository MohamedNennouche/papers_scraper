import scrapy
from scrapy.loader import ItemLoader


class arxivissues(scrapy.Spider):
    name = 'issue'
    start_urls = ['https://github.com/ML4Comm-Netw/Paper-with-Code-of-Wireless-communication-Based-on-DL/issues/15']

    def parse(self, response):
        for comments in response.css('td.d-block.comment-body.markdown-body.js-comment-body'):

            yield {'comments' : comments.css('p::text').getall()}