# -*- coding: utf-8 -*-
import datetime

nowTimeStamp = lambda: datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # http://stackoverflow.com/a/5215012/893511

print nowTimeStamp() # 2016-05-10_10-56-30

def today_YYYY_MM_DD():
    """ Return today's date as YYYY-MM-DD """ # http://stackoverflow.com/a/339013/893511         prepend zeros ---------------------v
    return str(datetime.date.today().year) + "-" + str(datetime.date.today().month).zfill(2) + "-" + str(datetime.date.today().day).zfill(2)
    
print today_YYYY_MM_DD() # 2016-05-10