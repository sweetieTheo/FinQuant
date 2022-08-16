from process.Implementation.StockSelection import StockSelection
from run.config import Path
from multiprocessing import Pool
import csv


if __name__ == '__main__':
    industry = '银行'
    trading_date = '2022-01-11'
    output_root = r'F:\数据\个股量化方案\test'

    file = open(Path.data_root + '\\stock_industry.csv', 'r')

    industries = {}
    for r in csv.DictReader(file):
        if r['industry'] not in industries:
            industries[r['industry']] = []
        industries[r['industry']].append(r['code'])

    p = StockSelection(category=industry,  # string, 分类
                       stock_list=industries[industry],  # list, 股票列表
                       trading_date=trading_date,  # string, 交易日期
                       stock_limit=3,  # int, 选取股票数量限制
                       strategies=['Top_marketValue'],  # list, 选股策略
                       output_root=output_root
                       )

    p.run()
