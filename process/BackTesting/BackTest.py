from classlibrary.BackTestor import BackTestor
from classlibrary.Stock import Stock
from datetime import datetime as dt
from classlibrary.Tool import Tool
from classlibrary.Portfolio import Portfolio
import csv
import time
import os


class BackTesting:
    def __init__(self,
                 stock_id,
                 strategy,
                 result_root,
                 action_root
                 ):
        self.stock = Stock(stock_id=stock_id)
        self.result_root = result_root
        self.action_root = action_root
        self.strategy = strategy
        self.portfolio = Portfolio()

    def run(self):
        t = time.time()
        print('正在回测，', self.stock.stock_id)

        if not os.path.exists(self.result_root + '\\' + dt.now().strftime('%Y-%m-%d')):
            os.makedirs(self.result_root + '\\' + dt.now().strftime('%Y-%m-%d'))

        output_file = open(self.result_root + '\\' + dt.now().strftime('%Y-%m-%d') + '\\回测-{0}-{1}.csv'.format(self.strategy, self.stock.stock_id), 'w')
        output_file.write('time,strategy,holding_period,stock_id,open_price,close_price,account_value\n')

        input_file = open(self.action_root + '\\' + self.strategy + '\\' + self.stock.stock_id + '.csv', 'r')

        count = 0
        morning_action = 'NA'
        # 文件必须按日期排序
        for r in csv.DictReader(input_file):
            count += 1
            if morning_action == 'buy' and self.stock.stock_id not in self.portfolio.holding:
                self.portfolio.long(stock_id=self.stock.stock_id, tstock=self.stock[Tool.std_date(r['date'])])
            elif morning_action == 'sell' and self.stock.stock_id in self.portfolio.holding:
                self.portfolio.short(stock_id=self.stock.stock_id, tstock=self.stock[Tool.std_date(r['date'])])

            morning_action = r['action']

            # 计算账户价值
            account_value = self.portfolio.cash
            for estate, num in self.portfolio.holding.items():
                account_value += num * self.stock[Tool.std_date(r['date'])].close_price

            output_file.write(r['date'] + ',' +
                              self.strategy + ',' +
                              ('N' if not self.portfolio.holding else 'Y') + ',' +
                              self.stock.stock_id + ',' +
                              str(self.stock[Tool.std_date(r['date'])].open_price) + ',' +
                              str(self.stock[Tool.std_date(r['date'])].close_price) + ',' +
                              str(account_value) + '\n'
                              )
        input_file.close()
        output_file.close()
        print(self.stock.stock_id, '回测结束，用时：', time.time() - t, '秒')
