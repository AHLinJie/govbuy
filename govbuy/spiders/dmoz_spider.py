from scrapy.spider import Spider
from ..items import DmozItem


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.baidu.com",
    ]

    def parse(self, response):
        items = []
        item = DmozItem()
        title = response.xpath('//title/text()').extract()[0]
        item['title'] = title
        items.append(item)
        return items
