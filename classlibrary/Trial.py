import baostock as bs
import pandas as pd
import os
from run.config import Path, Time
import csv
import time


class Bstock(object):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None):
        self.code = code
        self.start_date = start_date
        self.end_date = end_date
        self.lg = None
        self.method = {}

    def login(self):
        self.lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:' + self.lg.error_code)
        print('login respond  error_msg:' + self.lg.error_msg)

    @staticmethod
    def logout():
        bs.logout()

    def download(self, func):

        data_list = []
        rs = func()
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        stock = pd.DataFrame(data_list, columns=rs.fields)

