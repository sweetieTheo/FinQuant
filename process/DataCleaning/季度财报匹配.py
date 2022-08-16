from run.config import Path
from classlibrary.Tool import Tool
import csv
import os
import time


class ReportDataMatch:
    def __init__(self,
                 stock_id
                 ):
        self.stock_id = stock_id
        self.profit_data = {}

    def run(self):
        t = time.time()
        print(self.stock_id, '开始清洗')
        if not os.path.exists(Path.daily_root):
            os.makedirs(Path.daily_root)

        profit_file = open(Path.report_root + '\\profit_{}.csv'.format(self.stock_id), 'r')
        for r in csv.DictReader(profit_file):
            self.profit_data[Tool.std_date(r['statDate'])] = r
        profit_file.close()

        stock_file = open(Path.stock_root + '\\' + self.stock_id + '.csv', 'r')

        output_file = open(Path.daily_root + '\\' + self.stock_id + '.csv', 'w')

        header = False

        for r in csv.DictReader(stock_file):
            try:
                if not header:
                    output_file.write(','.join(r.keys()) + ',pubDate,totalShare' + '\n')
                    header = True
                date = Tool.std_date(r['date'])
                stat_date = Tool.get_last_day(date)
                totshare = self.profit_data[stat_date]['totalShare']
                public_date = 'Y' if self.profit_data[stat_date]['pubDate'] == r['date'] else 'N'
                output_file.write(','.join(r.values()) + ',' + public_date + ',' + totshare + '\n')
            except KeyError:
                continue
        print(self.stock_id, '清洗结束，用时：', time.time() - t, '秒')

