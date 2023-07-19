import time

import constant
import pymysql

def execute_sql(sql):
    conn = pymysql.connect(host=constant.host,
                           user=constant.user,
                           password=constant.password,
                           database=constant.database,
                           port=constant.port)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

def update_data_sql(id,count,remark):
    #"UPDATE yyslog SET ut = '2023-01-30 12:34:56',COUNT=3,remark='' WHERE id=3"
    utStr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return "UPDATE yyslog SET ut = '{}',COUNT={},remark='{}' WHERE id={}".format(utStr,count,remark,id)

def update_st_sql(id):
    stStr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return "UPDATE yyslog SET st = '{}' WHERE id={}".format(stStr,id)

if __name__ == '__main__':
    execute_sql(update_data_sql(3,0,"ssssss"))