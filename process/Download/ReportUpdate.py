from run.config import Path
import baostock as bs
import pandas as pd
import traceback
import time


class ReportUpdate:
    def __init__(self,
                 stock_id,
                 years,
                 bs
                 ):
        self.stock_id = stock_id
        self.years = years
        self.profit_list = []
        self.bs = bs
        self.profit_title = None

    def run(self):
        try:
            t = time.time()
            print('正在下载...{}'.format(self.stock_id))
            for year in self.years:
                for quarter in [1, 2, 3, 4]:
                    rs_profit = self.bs.query_profit_data(code=self.stock_id, year=year, quarter=quarter)
                    while (rs_profit.error_code == '0') & rs_profit.next():
                        self.profit_list.append(rs_profit.get_row_data())

                    if self.profit_title is None:
                        self.profit_title = rs_profit.fields
            result_profit = pd.DataFrame(self.profit_list, columns=self.profit_title)

            result_profit.to_csv(Path.data_root + '\\财报数据_季度\\result_profit_{0}.csv'.format(self.stock_id), encoding='gbk', index=False)
            print('数据下载完成，用时：', time.time() - t, '秒')
        except:
            traceback.print_exc()
