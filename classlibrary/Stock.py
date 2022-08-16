from run.config import Path, Time
from classlibrary.Tool import Tool
from collections import deque
import csv


class TStock:
    def __init__(self,
                 r
                 ):
        self.close_price = float(r['close']) if r['close'] != '' else 0  # 收盘价
        self.open_price = float(r['open']) if r['open'] != '' else 0  # 开盘价
        self.high = float(r['high']) if r['high'] != '' else 0  # 最高价
        self.low = float(r['low']) if r['low'] != '' else 0  # 最低价
        self.preclose = float(r['preclose']) if r['preclose'] != '' else 0  # 前交易日收盘价
        self.amount = float(r['amount']) if r['amount'] != '' else 0
        self.volume = float(r['volume']) if r['volume'] != '' else 0  # 交易量
        self.turn = float(r['turn']) if r['turn'] != '' else 0
        self.PE = float(r['peTTM']) if r['peTTM'] != '' else 0
        self.totshare = float(r['totalShare']) if r['totalShare'] != '' else 0
        self.mv = self.totshare * self.close_price



class Stock:
    def __init__(self,
                 stock_id  # str
                 ):
        self.stock_id = stock_id
        self.tvalues = {}

        file = open(Path.stock_root + '\\' + stock_id + '.csv', 'r')

        for r in csv.DictReader(file):
            self.tvalues[Tool.std_date(r['date'])] = TStock(r)
        file.close()

    def __getitem__(self, date):
        if date in self.tvalues:
            return self.tvalues[date]
        else:
            return 0

    def moving_average(self, period):

        ma_dict = {}
        container = deque(maxlen=period)
        for time, tstock in self.tvalues.items():
            container.append(tstock.close_price)
            if len(container) == period:
                ma_dict[time] = sum(container) / period
                container.popleft()

        return ma_dict
