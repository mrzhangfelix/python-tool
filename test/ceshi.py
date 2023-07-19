from time import sleep
import pymysql

def main():
    print("开始工作")
    conn = pymysql.connect(host='localhost', user='root', password='root', database='dev', port=3306)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user')
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()
