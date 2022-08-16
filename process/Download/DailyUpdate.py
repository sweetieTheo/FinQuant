from classlibrary.Download_BStock import Bstock
from run.config import Path, Time, Token


class DailyUpdate(object):
    def __init__(self,
                 start_date=None,
                 end_date=None
                 ):
        self.start_date = start_date
        self.end_date = end_date
        self.bs = Bstock(start_date=self.start_date, end_date=self.end_date)

    def run(self):
        # 股票列表
        self.bs.stock_info()

        # 股票日K数据
        self.bs.daily()

