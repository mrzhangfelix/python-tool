import time
from datetime import datetime
from time import sleep
import pymysql

def main():
    time_1 = '2020-03-02 23:00:00'
    time_2 = '2020-03-04 01:00:12'
    time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
    time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")
    total_seconds = (time_2_struct - time_1_struct).total_seconds()
    print('时间差为：{}'.format(seconds_to_hms(total_seconds)))
    print()


def seconds_to_hms(seconds_num):
    try:
        m, s = divmod(seconds_num, 60)
        h, m = divmod(m, 60)
        hms = "%02d:%02d:%02d" % (h, m, s)
        return hms
    except:
        print("转换失败")
        return seconds_num

if __name__ == '__main__':
    main()
