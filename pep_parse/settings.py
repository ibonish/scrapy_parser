from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
NAME = 'name'
STATUS = 'status'
NUMBER = 'number'
FORMAT = 'csv'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.{FORMAT}': {
        'format': FORMAT,
        'fields': [NUMBER, NAME, STATUS],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PATTERN = r'PEP (?P<number>\d+) – (?P<name>.+)'

LINK_XPATH = "//a[contains(@class, 'pep')]/@href"
TITLE_XPATH = "//h1[@class='page-title']/text()"
STATUS_CSS = 'dt:contains("Status")+dd abbr::text'

ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']

SPIDER_NAME = 'pep'

TABLE_HEADER = ('Статус', 'Количество')
TOTAL = 'Всего'
