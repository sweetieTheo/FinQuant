from collections import Counter
from classlibrary.Stock import Stock
from classlibrary.Strategies.FundamentalSelection import SelectionAlg
from classlibrary.Tool import Tool
import os


class StockSelection:
    def __init__(self,
                 category,  # string, 分类
                 stock_list,  # list, 股票列表
                 trading_date,  # string, 交易日期
                 stock_limit,  # int, 选取股票数量限制
                 strategies,  # list, 选股策略
                 output_root
                 ):
        self.category = category
        self.trading_date = Tool.std_date(trading_date)
        self.candidates = [Stock(stock_id=stock_id) for stock_id in stock_list]
        self.strategies = strategies
        self.stock_limit = stock_limit
        self.fundamentalAlg = SelectionAlg()
        self.output_root = output_root
        self.result = []

    def run(self):
        if not os.path.exists(os.path.abspath(self.output_root)):
            os.makedirs(os.path.abspath(self.output_root))
        output_file = open(self.output_root + '\\' + self.category + '.csv', 'w')
        output_file.write('trading_date,strategy,stock_id\n')

        # 对所有的策略循环，并储存临时结果
        for strategy in self.strategies:
            self.result.extend(self.fundamentalAlg[strategy](self.candidates, self.stock_limit, self.trading_date))

        # 计数
        voting = Counter(self.result)

        for stock_id, frequency in voting.most_common(self.stock_limit):
            output_file.write(self.trading_date.strftime('%Y-%m-%d') + ',' +
                              ','.join(self.strategies) + ',' +
                              stock_id + '\n'
                              )
        output_file.close()


