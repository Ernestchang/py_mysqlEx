# -*- coding: UTF-8 -*-  
'''
Created on 2017年5月28日

@author: Administrator
'''
import MySQLdb

conn = MySQLdb.Connect(
                       host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = 'bsker',
                       db = 'pysql',
                       charset = 'utf8'
                       )
cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()