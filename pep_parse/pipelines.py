import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        status = item['status']
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        downloads_dir = BASE_DIR / 'results'
        downloads_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_format = now.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{now_format}.csv'
        archive_path = downloads_dir / filename
        with open(archive_path, mode='w', encoding='utf-8') as file:
            header = ['STATUS', 'AMOUNT']
            pep_table = self.statuses.items()
            total = ['TOTAL', sum(self.statuses.values())]
            file_writer = csv.writer(
                file,
                dialect='unix',
                quoting=csv.QUOTE_MINIMAL
            )
            file_writer.writerows([
                header,
                *pep_table,
                total,
            ])
