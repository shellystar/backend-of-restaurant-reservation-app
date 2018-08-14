# -*- coding: UTF-8 -*-
import json

class request:
    def __init__(self, method='', requestURI='', contentType='', contentLength='', host='', data=''):
        self.Method = method
        self.RequestURI = requestURI
        self.ContentType = contentType
        self.ContentLength = contentLength
        self.Host = host
        self.Data = data

    def parse_request(self, requestJson):
        requestJson = json.loads(requestJson)
        self.Method = requestJson['Method']
        self.RequestURI = requestJson['RequestURI']
        self.ContentType = requestJson['ContentType']
        self.ContentLength = requestJson['ContentLength']
        self.Host = requestJson['Host']
        self.Data = requestJson['Data']

    def pack_request(self, requestJson):
        requestJson['Method'] = self.Method
        requestJson['RequestURI'] = self.RequestURI
        requestJson['ContentType'] = self.ContentType
        requestJson['ContentLength'] = self.ContentLength
        requestJson['Host'] = self.Host
        requestJson['Data'] = self.Data
        requestJson = json.dumps(requestJson)
        return requestJson

