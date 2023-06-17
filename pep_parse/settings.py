from pathlib import Path
from datetime import datetime as dt

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True
RESULS_DIR = 'results'

FEEDS = {
    RESULS_DIR + '/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

PEP_URL = 'peps.python.org'
BASE_DIR = Path(__file__).parent.parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DATETIME = dt.now().strftime(DATETIME_FORMAT)
