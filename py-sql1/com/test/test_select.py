# -*- coding: UTF-8 -*-  
'''
Created on 2017年5月28日 @author: Administrator
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

sql_insert = "insert into tb0(userid,username) values(9,'name9')"
sql_update= "update user set username='name91' where userid=9"
sql_delete = "delete from tb0 where userid<3"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()