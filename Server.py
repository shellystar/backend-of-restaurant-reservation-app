# -*- coding: UTF-8 -*-
import socket
from response import response
from request import request
from connect import connect
from search import SearchRestaurant
from appointment import insert_appointment
import os

sock = socket.socket()
sock.bind(('127.0.0.1', 3000))
sock.listen(5)
dbconn = connect()

while True:
    (conn, addr) = sock.accept()
    # new process
    print("connection succeed! ")

    ''''''
    pid = os.fork()
    if pid == 0:
        req = request()
        reqJson = conn.recv(1024)
        print(reqJson)

        if not reqJson:
            print ("recv returns 0")
        else:
            req.parse_request(reqJson)

        res = response()
        if (req.RequestURI == '/search'):
            res = SearchRestaurant(dbconn, req.Data['rName'])
        elif (req.RequestURI == '/appointment'):
            res = insert_appointment(dbconn, req.Data['rID'], req.Data['uID'], req.Data['tableType'],
                                     req.Data['startTime'], req.Data['duration'])
        resJson = {}
        resJson = res.pack_response(resJson)
        print(resJson)
        conn.send(resJson)

    elif pid > 0:
        conn.close()

    ##conn.send('hello client');
    ##conn.close();
