# -*- coding: UTF-8 -*-
import json

class response:
    def __init__(self, StatusCode='', ReasonPhrase='', ContentType='', ContentLength='', Data=''):
        self.StatusCode = StatusCode
        self.ReasonPhrase =ReasonPhrase
        self.ContentType = ContentType
        self.ContentLength = ContentLength
        self.Data = Data

    def parse_response(self, ResponseJson):
        ResponseJson = json.loads(ResponseJson)
        self.StatusCode = ResponseJson['StatusCode']
        self.ReasonPhrase = ResponseJson['ReasonPhrase']
        self.ContentType = ResponseJson['ContentType']
        self.ContentLength = ResponseJson['ContentLength']
        self.Data = ResponseJson['Data']

    def pack_response(self, ResponseJson):
        ResponseJson['StatusCode'] = self.StatusCode
        ResponseJson['ReasonPhrase'] = self.ReasonPhrase
        ResponseJson['ContentType'] = self.ContentType
        ResponseJson['ContentLength'] = self.ContentLength
        ResponseJson['Data'] = self.Data
        ResponseJson = json.dumps(ResponseJson)
        return ResponseJson