import pandas as pd
import tushare as ts
import csv


if __name__ == '__main__':
    pro = ts.pro_api('bb493246d0d9a014f0003cedbbdb6f45a6162ac71a4e1349396c493a')
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_csv('股票列表.csv')