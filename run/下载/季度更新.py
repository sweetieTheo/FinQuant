from classlibrary.Download_BStock import Bstock
from process.Download.ReportUpdate import ReportUpdate
from run.config import Path
import baostock as bs
from multiprocessing import Pool
import csv
import time


if __name__ == '__main__':
    # # 更新季度财务报表数据
    # process = Bstock()
    # process.quar_report_data()
    # pool = Pool(5)

    bs.login()
    file = open(Path.data_root + '\\stock_industry.csv', 'r')
    for r in csv.DictReader(file):
        p = ReportUpdate(stock_id=r['code'], years=range(2010, 2023), bs=bs)
        p.run()

    bs.logout()

