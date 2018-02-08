import scrapy
import pprint
pp = pprint.PrettyPrinter(indent=4)

class socialMediaSpider(scrapy.Spider):
	name = "social"

	def start_requests(self):
		urls = ['https://sfbay.craigslist.org/search/mar?query=social+media']

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		links = response.css('#sortable-results .rows .result-row .result-image::attr(href)').extract()

		for each in links:
			href = response.urljoin(each)
			yield response.follow(href, self.parse_page)

	def parse_page(self, response):
		link = response.css('.body header .replylink a::attr(href)').extract_first()
		if link is not None:
			new_link = 'https://sfbay.craigslist.org' + link
			href = response.urljoin(new_link)
			yield response.follow(href, self.parse_info)

	def parse_info(self, response):
		text = response.css('body').extract_first()
		print(text)