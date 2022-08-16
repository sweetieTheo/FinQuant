from process.Implementation.CrossMA import CrossMA
from run.config import Path
from multiprocessing import Pool
import csv


if __name__ == '__main__':
    file = open(Path.data_root + '\\stock_industry.csv', 'r')
    short_period = 5
    long_period = 30
    pool = Pool(60)
    for r in csv.DictReader(file):
        for short_period in [5, 10]:
            for long_period in [30, 60, 90]:
                process = CrossMA(stock_id=r['code'],
                                  short_period=short_period,
                                  long_period=long_period,
                                  action_root=Path.action_root
                                  )
                pool.apply_async(process.run)
    pool.close()
    pool.join()

