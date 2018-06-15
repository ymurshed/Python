# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from collections import namedtuple
from urllib.request import Request, urlopen

class ServiceCaller(object):
    def __init__(self):
        self.surl = 'http://localhost:58364/Subjects/api/Subjects/98D723E7-0FF4-4CC7-89B8-AB3C09755BBC/SubjectSchedules'
        print(self.surl)
        
    def get_data(self):
        try:
            request = Request(self.surl)
            response = urlopen(request)
            data = response.read().decode('utf-8')
            x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            print(x.visitName)
            
            for item in x:
                print(item)
                #print(item.subjectVisitId + ' ', item.visitName + ' ' + item.nextVisitDate + ' ' \
                      #+ item.visitNotificationMinutes)
            
        except Exception as e:
            print('service calling error!')
            
if __name__ == "__main__":
    caller = ServiceCaller()
    caller.get_data()