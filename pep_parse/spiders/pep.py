import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_URL]
    start_urls = ['https://' + PEP_URL + '/']

    def parse(self, response):
        all_pep = response.css(
            'section[id=numerical-index] tr td:nth-child(2) a::attr(href)'
        )
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
