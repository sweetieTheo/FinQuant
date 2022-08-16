from classlibrary.Stock import Stock
import time
import os
import traceback


class CrossMA:
    def __init__(self,
                 stock_id,
                 short_period,
                 long_period,
                 action_root
                 ):
        self.short_period = short_period
        self.long_period = long_period
        self.stock = Stock(stock_id=stock_id)
        self.short_ma = self.stock.moving_average(short_period)
        self.long_ma = self.stock.moving_average(long_period)
        self.action_root = action_root + '\\交叉移动平均{0}vs.{1}'.format(short_period, long_period)

    def run(self):
        try:
            print('开始制作：长短期交叉移动平均方案，', self.stock.stock_id)
            t = time.time()

            if not os.path.exists(self.action_root):
                os.makedirs(self.action_root)

            output_file = open(self.action_root + '\\{}.csv'.format(self.stock.stock_id), 'w')
            output_file.write('stock_id,date,{0}-daysMA,{1}-daysMA,action\n'.format(self.short_period, self.long_period))

            for timestamp, longMA in self.long_ma.items():
                if self.short_ma[timestamp] < longMA:
                    output_file.write(self.stock.stock_id + ',' + timestamp.strftime('%Y-%m-%d') + ',' + str(self.short_ma[timestamp]) + ',' + str(longMA) + ',sell\n')
                elif self.short_ma[timestamp] > longMA:
                    output_file.write(self.stock.stock_id + ',' + timestamp.strftime('%Y-%m-%d') + ',' + str(self.short_ma[timestamp]) + ',' + str(longMA) + ',buy\n')
                else:
                    output_file.write(self.stock.stock_id + ',' + timestamp.strftime('%Y-%m-%d') + ',' + str(self.short_ma[timestamp]) + ',' + str(longMA) + ',hold\n')

            print(self.stock.stock_id, '制作完成，用时：', time.time() - t, '秒')
        except:
            traceback.print_exc()

