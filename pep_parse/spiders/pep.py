import re

import scrapy

from ..items import PepParseItem
from ..settings import ALLOWED_DOMAINS, SPIDER_NAME


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        all_links = response.xpath(
            "//a[contains(@class, 'pep')]/@href"
        ).getall()
        for link in all_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath(
            "//h1[@class='page-title']/text()"
        ).get()
        pattern = r'PEP (?P<number>\d+) – (?P<name>.+)'
        text_match = re.search(pattern, title)
        status = response.xpath(
            "//dt[contains(text(), 'Sta')]/following-sibling::dd/abbr/text()"
        ).get()
        yield PepParseItem(dict(
            number=text_match.group('number'),
            name=text_match.group('name'),
            status=status
        ))
