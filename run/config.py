from datetime import datetime
import math


class Path:
    data_root = r'F:\数据'
    tmp = r'C:\Users\WIN10\Desktop\python\数据\输出\tmp'
    insert = r'C:\Users\WIN10\Desktop\python\算法\run\脚本\上传脚本'
    create = r'C:\Users\WIN10\Desktop\python\算法\run\脚本\建表脚本'
    stock_root = data_root + '\\股市数据_代码'
    daily_root = data_root + '\\股市数据_日期'
    report_root = data_root + '\\财报数据'
    result_root = data_root + '\\回测结果'
    action_root = data_root + '\\个股量化方案'


class Time:
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_year = datetime.now().year
    current_quarter = math.floor(datetime.now().month / 3)


class Token:
    tutoken = 'bb493246d0d9a014f0003cedbbdb6f45a6162ac71a4e1349396c493a'
    host = 'localhost'
    user = 'root'
    pwd = 'lxh310797'
    db = 'quant_finance'


# python中时间日期格式化符号：
# % y 两位数的年份表示（00 - 99）
# % Y 四位数的年份表示（000 - 9999）
# % m 月份（01 - 12）
# % d 月内中的一天（0 - 31）
# % H 24小时制小时数（0 - 23）
# % I 12小时制小时数（01 - 12）
# % M 分钟数（00 = 59）
# % S 秒（00 - 59）
# % a 本地简化星期名称
# % A 本地完整星期名称
# % b 本地简化的月份名称
# % B 本地完整的月份名称
# % c 本地相应的日期表示和时间表示
# % j 年内的一天（001 - 366）
# % p 本地A.M.或P.M.的等价符
# % U 一年中的星期数（00 - 53）星期天为星期的开始
# % w 星期（0 - 6），星期天为星期的开始
# % W 一年中的星期数（00 - 53）星期一为星期的开始
# % x 本地相应的日期表示
# % X 本地相应的时间表示
# % Z 当前时区的名称
# % % % 号本身
