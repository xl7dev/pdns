#!/usr/bin/env python
# encoding: utf-8

"""
@author: xl7dev
"""
import pymysql
import datetime


class MysqlDB:
    def __init__(self, host, user, pwd, port, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db, charset='utf8')
        self.cursor = self.conn.cursor()

    def insert(self, name, type, value):
        first = last = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = """INSERT INTO pdns (name,type,value,first,last,count) VALUES ('{0}','{1}','{2}','{3}','{4}',1) ON DUPLICATE KEY UPDATE count=count+1,first = if (unix_timestamp(first) > unix_timestamp('{5}'), '{6}', first),last = if (unix_timestamp(last) < unix_timestamp('{7}'), '{8}', last)""".format(
            name, type, value, first, last, first, first, last, last)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("[-] {0} {1} {2} {3}".format(name, type, value, e))
            self.conn.rollback()


if __name__ == "__main__":
    demo = MysqlDB()
    demo.insert('www.a.shifen.com', 'A', '61.135.169.121')