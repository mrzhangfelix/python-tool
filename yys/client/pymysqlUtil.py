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

def update_data_sql(id,ut,count,remark):
    #"UPDATE yyslog SET ut = '2023-01-30 12:34:56',COUNT=3,remark='' WHERE id=3"
    utStr=time.strptime(ut,'%Y-%m-%d %H:%M:%S')
    return "UPDATE yyslog SET ut = {},COUNT={},remark={} WHERE id={}".format(utStr,count,remark,id)

def update_st_sql(id,st):
    stStr=time.strptime(st,'%Y-%m-%d %H:%M:%S')
    return "UPDATE yyslog SET st = {}WHERE id={}".format(stStr,id)