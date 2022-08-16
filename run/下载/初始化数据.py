from classlibrary.Download_BStock import Bstock
import baostock as bs
from run.config import Path, Time
import csv


if __name__ == '__main__':
    bs.login()
    # 初始化股票信息
    # Bstock.stock_info()
    #
    # # 初始化股票日K数据
    # Bstock.init_stock()

    # 初始化季度财务报表数据
    data_querys = ['profit',
                   'operation', 'growth', 'balance', 'cash_flow', 'dupont']

    for data_query in data_querys:
        file = open(Path.data_root + '\\stock_industry.csv', 'r')
        for r in csv.DictReader(file):
            p = Bstock(code=r['code'], bs=bs)
            p.quar_report_data(data_type=data_query, years=range(2010, 2023), quarters=[1, 2, 3, 4])
        file.close()

    bs.logout()
