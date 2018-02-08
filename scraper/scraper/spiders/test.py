import re
import scrapy


# item class included here
class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    attr = scrapy.Field()


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["craigslist.org"]
    start_urls = [
    "http://chicago.craigslist.org/search/vgm?"
    ]

    BASE_URL = 'http://chicago.craigslist.org/'

    def parse(self, response):
        links = response.xpath('//a[@class="hdrlnk"]/@href').extract()
        print(links)
        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)

    def parse_attr(self, response):
        match = re.search(r"(\w+)\.html", response.url)
        if match:
            item_id = match.group(1)
            print(item_id)
            url = self.BASE_URL + "reply/chi/vgm/" + item_id

            item = DmozItem()
            item["link"] = response.url

            return scrapy.Request(url, meta={'item': item}, callback=self.parse_contact)

    def parse_contact(self, response):
        item = response.meta['item']
        item["attr"] = "".join(response.xpath("//div[@class='anonemail']//text()").extract())
        return item