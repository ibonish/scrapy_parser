import csv
import datetime as dt
from collections import Counter

from .settings import (BASE_DIR, DATETIME_FORMAT, FORMAT, RESULTS,
                       TABLE_HEADER, TOTAL)


class PepParsePipeline:
    def __init__(self) -> None:
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = Counter()

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.{FORMAT}'
        file_path = self.results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv.writer(
                f, csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            ).writerows((
                TABLE_HEADER,
                *self.status_counts.items(),
                (TOTAL, sum(self.status_counts.values())),
            ))
