from process.DataCleaning.季度财报匹配 import ReportDataMatch
from multiprocessing import Pool
from run.config import Path
import csv


if __name__ == '__main__':

    pool = Pool(20)
    file = open(Path.data_root + '\\stock_industry.csv', 'r')
    for r in csv.DictReader(file):
        p = ReportDataMatch(stock_id=r['code'])
        pool.apply_async(p.run)
    pool.close()
    pool.join()

