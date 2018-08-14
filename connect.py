# -*- coding: UTF-8 -*-
import MySQLdb

def connect():
    conn = MySQLdb.connect(host='localhost', user='root', passwd='pwd', db='dbname', charset="utf8")
    #print ("connection successful")
    return conn