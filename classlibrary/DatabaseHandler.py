import pymysql
import csv
import traceback


class DatabaseHandler(object):
    def __init__(self,
                 host=None,
                 user=None,
                 pwd=None,
                 db=None
                 ):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def connect(self):
        connection = pymysql.connect(host=self.host, user=self.user, passwd=self.pwd, db=self.db)
        return connection

    def execute(self, sql):
        return

    def upload(self, sql_path, file_path):
        connection = self.connect()

        sql_file = open(sql_path)
        sql = sql_file.read()
        file = open(file_path, 'r')
        file.readline()
        data = []
        for r in csv.reader(file):

            data.append(tuple([i if i != '' else None for i in r]))
            # 分行数上传
            if len(data) >= 1000:
                try:
                    cursor = connection.cursor()
                    cursor.executemany(sql, data)
                    cursor.close()
                    connection.commit()
                    data = []
                except:
                    traceback.print_exc()
                    break
        try:
            cursor = connection.cursor()
            cursor.executemany(sql, data)
            cursor.close()
            connection.commit()
        except:
            traceback.print_exc()

        connection.close()
        print('上传结束 ', file_path)

    def download(self, sql, file_path):
        return

