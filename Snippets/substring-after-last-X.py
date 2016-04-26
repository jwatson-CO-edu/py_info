# -*- coding: utf-8 -*-
def last_X_to_end(longStr,charX):
    """ Return the portion of 'longStr' that is occurs after the last instance of 'charX' is present, otherwise return 'longStr' """
    rtnStr = ''
    charDex = -1
    while longStr[charDex] != charX and charDex >= -len(longStr):
        rtnStr = longStr[charDex] + rtnStr
        charDex -= 1
    return rtnStr