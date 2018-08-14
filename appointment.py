# -*- coding: UTF-8 -*-
import MySQLdb
from response import response

#duration <= 4
def check_remaining(info, startTime, duration):
    for i in range(startTime-15, min(startTime+duration-16,len(info)-1)):
        if info[i] == 0:
            return -1
    return 0

def update_remaining(info,rid,tableType,startTime,duration):
    time = ['time17', 'time18', 'time19', 'time20']
    sql = 'UPDATE Available SET '
    i = 0
    for i in range(startTime - 15, min(startTime + duration - 15, 5)):
        print(time[i-2])
        print(info[0][i])
        sql = sql + time[i-2] + " = %d, " %(info[0][i]-1)
    i = i + 1
    sql = sql + time[i - 2] + " = %d " % (info[0][i] - 1)
    sql = sql + "WHERE rid = '%d' AND tableType = '%d'"%(rid,tableType)
    return sql

def insert_appointment(conn,rid,uid,tableType,startTime,duration):
    res = response()
    cur = conn.cursor()
    find_restTable_sql = """
                        SELECT rID, tableType, time17, time18, time19, time20
                        FROM Available
                        WHERE rid = '%d' AND tableType = '%d'"""% (rid,tableType)
    cur.execute(find_restTable_sql)
    find_restTable_result = cur.fetchall()
    #print(find_restTable_result)

    if(check_remaining(find_restTable_result, startTime, duration) == -1):
        print("no remaining")
        res.StatusCode = '404'
        res.ReasonPhrase = 'no remaining'

    insert_sql = """INSERT INTO Appointment
                    VALUES('%d','%s','%d','%d','%d')""" % (rid,uid,tableType,startTime,duration)

    update_remaining_sql = update_remaining(find_restTable_result,rid,tableType,startTime,duration)
    print(update_remaining_sql)

    try:
        cur.execute(insert_sql)
        cur.execute(update_remaining_sql)
        conn.commit()
        res.StatusCode = '200'
        res.ReasonPhrase = 'successfully inserted'
    except MySQLdb.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        res.StatusCode = '404'
        res.ReasonPhrase = 'fail to insert'

    return res
