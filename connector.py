#!/usr/bin/python
# -*- coding: utf-8 -*-
# 连接数据库

import pymysql

config = {
    'host': '118.24.155.143',
    'port': 3306,
    'user': 'root',
    'passwd': 'lizhao',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()
conn.select_db('JuziMi')

tableName = 'juzimi'


def select_count():
    try:
        count = cursor.execute('select * from %s' % tableName)
        print cursor.rowcount

    except:
        import traceback
        traceback.print_exc()
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

def insert_list(l=[]):
    try:
        for i in range(len(l)):
            count = cursor.execute('INSERT INTO juzimi (content) VALUES ("%s")' %l[i])
        print cursor.rowcount

    except:
        import traceback
        traceback.print_exc()
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
