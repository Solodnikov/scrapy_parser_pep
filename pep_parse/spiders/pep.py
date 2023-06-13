import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        # Находим все ссылки.
        all_pep = response.css('section[id=numerical-index] tbody a::attr(href)')
        # Перебираем ссылки по одной.
        for pep_link in all_pep:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get().strip()
        data = {
            'name': name,
            'number': name.split('–')[0].replace('PEP', '').strip(),
            'status': response.css('dt:contains("Status") + dd').
            css('abbr::text').get()
        }
        yield PepParseItem(data)
