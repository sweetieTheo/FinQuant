from run.config import Path, Time, Token
from classlibrary.Tool import Tool
import tushare as ts
import pandas as pd
import time
import os


class TuDownLoad(object):
    def __init__(self,
                 ts_code=None,
                 start_date=None,
                 end_date=None):
        self.ts_code = ts_code
        self.pro = ts.pro_api(token=Token.tutoken)
        self.start_date = start_date
        self.end_date = end_date

    # 日线全股数据下载
    def daily(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        print('正在下载日线数据...')
        datelist = Tool.enum_date(start_date=self.start_date, end_date=self.end_date)
        for date in datelist:
            print(date)
            data = self.pro.daily(trade_date=date.replace('-', ''))
            data.to_csv(path + '\\{}.csv'.format(date), index=False)
            time.sleep(0.5)
        print('日线数据下载完成，路径：', Path.tmp)

    # 股票列表下载
    def stock_list(self):
        print('正在更新上市股票列表...')
        dataL = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,market,is_hs,list_status,list_date,delist_date')
        dataD = self.pro.stock_basic(exchange='', list_status='D', fields='ts_code,symbol,name,area,industry,market,is_hs,list_status,list_date,delist_date')
        dataP = self.pro.stock_basic(exchange='', list_status='P', fields='ts_code,symbol,name,area,industry,market,is_hs,list_status,list_date,delist_date')
        data = pd.concat([dataL, dataD, dataP])
        data.to_csv(Path.data_root + '\\股票列表.csv', encoding='gbk', index=False)
        print('上市股票列表已更新完毕，路径：', Path.data_root)
