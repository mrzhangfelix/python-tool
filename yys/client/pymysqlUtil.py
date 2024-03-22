import time
from datetime import datetime

import constant
import pymysql

stStr=''
utStr=''
def execute_sql(sql):
    pass
    # conn = pymysql.connect(host=constant.host,
    #                        user=constant.user,
    #                        password=constant.password,
    #                        database=constant.database,
    #                        port=constant.port)
    # cursor = conn.cursor()
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # conn.commit()
    # cursor.close()
    # conn.close()

def update_data(id,count,remark):
    #"UPDATE yyslog SET ut = '2023-01-30 12:34:56',COUNT=3,remark='' WHERE id=3"
    global utStr
    utStr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    sql="UPDATE yyslog SET ut = '{}',COUNT={},remark='{}',duration='{}' WHERE id={}".format(utStr,count,remark,get_duration(),id)
    execute_sql(sql)

def update_st(id):
    global stStr
    stStr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    sql= "UPDATE yyslog SET st = '{}' WHERE id={}".format(stStr,id)
    execute_sql(sql)

def get_duration():
    # time_1 = '2020-03-02 23:00:00'
    # time_2 = '2020-03-04 01:00:12'
    time_1_struct = datetime.strptime(stStr, "%Y-%m-%d %H:%M:%S")
    time_2_struct = datetime.strptime(utStr, "%Y-%m-%d %H:%M:%S")
    total_seconds = (time_2_struct - time_1_struct).total_seconds()
    return seconds_to_hms(total_seconds)

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
    update_data(3,0,"ssssss")