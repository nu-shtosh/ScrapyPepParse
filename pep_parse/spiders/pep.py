import scrapy
from pep_parse.items import PepItem

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        find_sctn = response.css('section.numerical-index')
        find_dv = find_sctn.css('div.table-wrapper')
        find_tbd = find_dv.css('tr')

        for pep in response.css('class.numerical-index'):
            data = {
                'number': pep.css('span.text::text').get(),
                'name': pep.css('small.author::text').get(),
                'status': pep.css('a.tag::text').getall(),
            }
            yield PepItem(data)
