# -*- coding: utf-8 -*-
import datetime

nowTimeStamp = lambda: datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # http://stackoverflow.com/a/5215012/893511

print nowTimeStamp()