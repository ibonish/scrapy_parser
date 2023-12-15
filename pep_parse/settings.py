from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_NAME = 'pep'

ALLOWED_DOMAINS = ['peps.python.org']
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
FORMAT = 'csv'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.{FORMAT}': {
        'format': FORMAT,
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
TABLE_HEADER = ('Статус', 'Количество')
TOTAL = 'Всего'
