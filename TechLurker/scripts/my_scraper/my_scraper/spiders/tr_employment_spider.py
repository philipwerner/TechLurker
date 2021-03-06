import scrapy
from scrapy import Request
from TechLurker.scripts.my_scraper.my_scraper.items import TechRepulicItem


class Tr_employment(scrapy.Spider):
    name = "trEmployment"
    allowed_domains = ["techrepublic.com"]
    start_urls = ["https://www.techrepublic.com/forums/it-employment/"]

    def parse(self, response):
        posts = response.xpath('//div[@class="discussionTitle"]/a/@href').extract()
        for post in posts:
            absolute_url = post
            yield Request(absolute_url, callback=self.parse_page)

        next_pg = response.xpath('//section[@class="discussion-pagination"]/a/@href').extract()[-1]
        yield Request(next_pg, callback=self.parse)

    def parse_page(self, response):
        item = TechRepulicItem()
        item['title'] = response.xpath('//h3[@data-forum-post]/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="post"]/text()').extract()
        item['votes'] = response.xpath('//span[@class="count"]/text()').extract()[0]
        item['from_forum'] = 'employment_discussion'
        yield item
