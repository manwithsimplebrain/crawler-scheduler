import scrapy
from scrapy_app.items import QuoteSpiderItem

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuoteSpiderItem()
            item["text"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()
            item["tags"] = quote.css("div.tags a.tag::text").getall()
            yield item
            
        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page:
        #     yield response.follow(next_page, self.parse)
