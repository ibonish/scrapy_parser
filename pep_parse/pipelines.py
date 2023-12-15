import csv
import datetime as dt
from collections import Counter

from .settings import (BASE_DIR, DATETIME_FORMAT, FORMAT, RESULTS,
                       STATUS, TABLE_HEADER, TOTAL)


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = Counter()

    def process_item(self, item, spider):
        self.status_counts[item[STATUS]] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.{FORMAT}'
        RESULTS_DIR = BASE_DIR / RESULTS
        RESULTS_DIR.mkdir(exist_ok=True)
        file_path = RESULTS_DIR / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv.writer(
                f, csv.unix_dialect,
            ).writerows([
                TABLE_HEADER,
                *self.status_counts.items(),
                (TOTAL, sum(self.status_counts.values())),
            ])
