import csv
import datetime
import math


class Tool:
    def __init__(self):
        pass

    @staticmethod
    def std_date(strdate):
        if '/' not in strdate and '-' not in strdate:
            date = strdate[0:4] + '-' + strdate[4:6] + '-' + strdate[6:8]
        else:
            date = strdate.replace('/', '-')

        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return date

    # 枚举两个日期间所有日期
    @staticmethod
    def enum_date(start_date, end_date):
        date_list = []
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        while start_date <= end_date:
            date = start_date.strftime('%Y-%m-%d')
            date_list.append(date)
            start_date += datetime.timedelta(days=1)
        return date_list

    @staticmethod
    def data_generator(path, keys):
        file = open(path, 'r')
        data = {}
        for r in csv.DictReader(file):
            data[','.join(r[key] for key in keys)] = r
        return data

    @staticmethod
    def add_days(date, days):
        return date + datetime.timedelta(days=days)

    @staticmethod
    def get_current_day(date, dtype='quarter'):
        if dtype == 'quarter':
            quarter = math.ceil(date.month / 3)
            return datetime.datetime(year=date.year if quarter < 4 else date.year + 1, month=quarter * 3 + 1 if quarter < 4 else 1, day=1) - datetime.timedelta(days=1)
        if dtype == 'month':
            return datetime.datetime(year=date.year if date.month < 12 else date.year + 1, month=date.month if date.month < 12 else 1, day=1) - datetime.timedelta(days=1)
        if dtype == 'year':
            return datetime.datetime(year=date.year + 1, month=1, day=1) - datetime.timedelta(days=1)

    @staticmethod
    def get_last_day(date, dtype='quarter'):
        if dtype == 'quarter':
            quarter = math.ceil(date.month / 3)
            return datetime.datetime(year=date.year, month=(quarter - 1) * 3 + 1 if quarter > 1 else 1, day=1) - datetime.timedelta(days=1)
        if dtype == 'month':
            return datetime.datetime(year=date.year, month=date.month, day=1) - datetime.timedelta(days=1)
        if dtype == 'year':
            return datetime.datetime(year=date.year, month=1, day=1) - datetime.timedelta(days=1)