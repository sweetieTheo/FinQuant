import baostock as bst
import pandas as pd
import os
from run.config import Path, Time
import csv
import time


class Bstock(object):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 bs=None):
        self.code = code
        self.start_date = start_date
        self.end_date = end_date
        self.bs = bs
        self.data_querys = {'profit':self.profit_data,
                            'operation': self.operation_data,
                            'growth': self.growth_data,
                            'balance': self.balance_data,
                            'cash_flow': self.cash_flow_data,
                            'dupont': self.dupont_data
                            }

    # 初始化股票日K数据
    @staticmethod
    def init_stock():
        t = time.time()
        print('更新A股日线数据... start_date:', '2010-01-01', ', end_date: ', Time.current_date)
        lg = bst.login()
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)
        file = open(Path.data_root + '\\stock_industry.csv', 'r')

        if not os.path.exists(Path.data_root + '\\股市数据_全量'):
            os.makedirs(Path.data_root + '\\股市数据_全量')

        for r in csv.DictReader(file):
            rs = bst.query_history_k_data_plus(r['code'], 'date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST,peTTM,pbMRQ,psTTM,pcfNcfTTM',
                                               start_date='2010-01-01', end_date=Time.current_date,
                                               frequency="d", adjustflag="3")

            data_list = []
            while (rs.error_code == '0') & rs.next():
                # 获取一条记录，将记录合并在一起
                data_list.append(rs.get_row_data())
            result = pd.DataFrame(data_list, columns=rs.fields)

            # 结果集输出到csv文件
            result.to_csv(Path.data_root + '\\股市数据_全量\\{}.csv'.format(r['code']), index=False)
            print('更新完毕，用时：', time.time() - t, '秒，路径：', Path.data_root + '\\股市数据_全量\\{}.csv'.format(r['code']))

        bst.logout()

    # 日常更新日K数据
    def daily(self):
        t = time.time()
        print('更新A股日线数据... date:', self.end_date)
        file = open(Path.data_root + '\\stock_industry.csv', 'r')

        if not os.path.exists(Path.data_root + '\\股市数据_全量'):
            os.makedirs(Path.data_root + '\\股市数据_全量')

        title = None
        data_list = []
        for r in csv.DictReader(file):
            print(r['code'])
            rs = self.bs.query_history_k_data_plus(r['code'], 'date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST,peTTM,pbMRQ,psTTM,pcfNcfTTM',
                                                   start_date=self.start_date, end_date=self.end_date,
                                                   frequency="d", adjustflag="3")
            if title is None:
                title = rs.fields
            while (rs.error_code == '0') & rs.next():
                # 获取一条记录，将记录合并在一起
                data_list.append(rs.get_row_data())

        result = pd.DataFrame(data_list, columns=title)

        # 结果集输出到csv文件
        result.to_csv(Path.data_root + '\\股市数据_日\\{}.csv'.format(Time.current_date), index=False)
        print('更新完毕，用时：', time.time() - t, '秒，路径：', Path.data_root + '\\股市数据_日\\{}.csv'.format(Time.current_date))

    # 更新股票列表
    @staticmethod
    def stock_info():
        t = time.time()
        print('更新股票列表及行业...')
        lg = bst.login()

        rs = bst.query_stock_basic()

        # 打印结果集
        stock_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            stock_list.append(rs.get_row_data())
        stock = pd.DataFrame(stock_list, columns=rs.fields)

        rs = bst.query_stock_industry()
        stock_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            stock_list.append(rs.get_row_data())
        industry = pd.DataFrame(stock_list, columns=rs.fields)

        result = pd.merge(stock, industry, on=['code', 'code_name'])
        bst.logout()
        result.to_csv(Path.data_root + '\\stock_industry.csv', index=False, encoding='gbk')
        print('更新完毕，用时：', time.time() - t, '秒，路径：', Path.data_root + '\\stock_industry.csv')

    # 季度更新财务报表数据
    def quar_report_data(self, data_type, years, quarters):
        t = time.time()
        print('开始下载本季度财务报表...', self.code)
        if not os.path.exists(Path.data_root + '\\财报数据_季度'):
            os.makedirs(Path.data_root + '\\财报数据_季度')

        rs_title = None
        rs_list = []

        # 查询季频估值指标盈利能力
        print('正在下载...{}'.format(self.code))
        for year in years:
            for quarter in quarters:
                rs = self.data_querys[data_type](year=year, quarter=quarter)
                while (rs.error_code == '0') & rs.next():
                    rs_list.append(rs.get_row_data())

                if rs_title is None:
                    rs_title = rs.fields

        result = pd.DataFrame(rs_list, columns=rs_title)

        # 结果集输出到csv文件
        result.to_csv(Path.data_root + '\\财报数据_季度\\{0}_{1}.csv'.format(data_type, self.code), encoding='gbk', index=False)

        print('更新完毕，用时：', time.time() - t, '秒，路径：', Path.data_root + '\\财报数据_季度\\{0}_{1}.csv'.format(data_type, self.code))

    # 查询季频估值指标盈利能力
    def profit_data(self, year, quarter):
        return self.bs.query_profit_data(code=self.code, year=year, quarter=quarter)

    # 营运能力
    def operation_data(self, year, quarter):
        return self.bs.query_operation_data(code=self.code, year=year, quarter=quarter)

    # 成长能力
    def growth_data(self, year, quarter):
        return self.bs.query_growth_data(code=self.code, year=year, quarter=quarter)

    # 偿债能力
    def balance_data(self, year, quarter):
        return self.bs.query_balance_data(code=self.code, year=year, quarter=quarter)

    # 季频现金流量
    def cash_flow_data(self, year, quarter):
        return self.bs.query_cash_flow_data(code=self.code, year=year, quarter=quarter)

    # 查询杜邦指数
    def dupont_data(self, year, quarter):
        return self.bs.query_dupont_data(code=self.code, year=year, quarter=quarter)

