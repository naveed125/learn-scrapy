import scrapy
from scrapy.linkextractors import LinkExtractor

class ReutersSpider(scrapy.Spider):
    name = "reuters"
    allowed_domains = ["reuters.com"]
    start_urls = ["https://www.reuters.com/site-search/?query=solid+state+batteries"]

    def parse(self, response) -> None:

        link_extractor = LinkExtractor()
        links = link_extractor.extract_links(response)

        for link in link_extractor.extract_links(response):

            yield {
                'text': link.text,
                'url': link.url
            }

