import re

import scrapy

from ..items import PepParseItem
from ..settings import (ALLOWED_DOMAINS, LINK_XPATH, NAME, NUMBER, PATTERN,
                        SPIDER_NAME, START_URLS, STATUS, STATUS_CSS,
                        TITLE_XPATH)


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_links = response.xpath(LINK_XPATH).getall()
        for link in all_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath(TITLE_XPATH).get()
        text_match = re.search(PATTERN, title)
        status = response.css(STATUS_CSS).get()
        yield PepParseItem(
            {
                NUMBER: text_match.group(NUMBER),
                NAME: text_match.group(NAME),
                STATUS: status
            }
        )
