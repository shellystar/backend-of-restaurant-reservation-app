# -*- coding: UTF-8 -*-
import MySQLdb
from response import response

def SearchRestaurant(conn, rName):
    sql = """select Restaurant.rID, rName, rAddr, rPic, tableType, time17, time18, time19, time20
             from Restaurant natural join Available
             where rName = '%s'""" % (rName)
    search = conn.cursor()
    search.execute(sql)
    result = search.fetchall()

    res = response()

    if not len(result):
        res.StatusCode = '404'
        res.ReasonPhrase = 'Restaurant ID Not Found'
    else:
        res.StatusCode = '200'
        res.ReasonPhrase = 'Search OK'


    dict = {'rID':'', 'rName':'', 'rAddr':'', 'rPic':'', 'tableInfo': []}
    dict['rID'] = result[0][0]
    dict['rName'] = result[0][1]
    dict['rAddr'] = result[0][2]
    dict['rPic'] = result[0][3]
    for rInfo in result:
        tmp = []
        tmp.append(rInfo[5])
        tmp.append(rInfo[6])
        tmp.append(rInfo[7])
        tmp.append(rInfo[8])
        dict['tableInfo'].append(tmp)

    res.Data = dict

    return res



