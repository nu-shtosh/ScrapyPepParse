import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):

        all_peps = response.css('a.reference.external::attr(href)')
        for pep in all_peps:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):

        data = {
            'number': response.css('dt:contains("PEP") + dd::text').get(),
            'name': response.css('dt:contains("Title") + dd::text').get(),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
