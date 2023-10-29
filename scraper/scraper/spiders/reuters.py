import scrapy


class ReutersSpider(scrapy.Spider):
    name = "reuters"
    allowed_domains = ["reuters.com"]
    start_urls = ["https://reuters.com"]

    def parse(self, response) -> None:
        for news in response.css('div.media-story-card__body__3tRWy'):

            title = news.css('a.text__text__1FZLe::text').get()
            url = news.css('a.text__text__1FZLe').attrib['href']

            if url == '/world/':
                continue

            yield {
                'title': title,
                'url': url
            }

