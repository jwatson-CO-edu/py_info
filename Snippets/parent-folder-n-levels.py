# -*- coding: utf-8 -*-
import os

def parent_folder(path, nLevelsUp):
    """ Return the containing directory that is 'nLevelsUp' from 'path' """
    if nLevelsUp == 0:
        return path
    else:
        return parent_folder(os.path.dirname(path), nLevelsUp-1)
        
def last_X_to_end(longStr,charX):
    """ Return the portion of 'longStr' that is occurs after the last instance of 'charX' is present, otherwise return 'longStr' """
    rtnStr = ''
    charDex = -1
    while longStr[charDex] != charX and charDex >= -len(longStr):
        rtnStr = longStr[charDex] + rtnStr
        charDex -= 1
    return rtnStr
    
def parent_folder_name_only(path, nLevelsUp):
    """ Return the name of the containing directory that is 'nLevelsUp' from 'item' """
    return last_X_to_end( parent_folder(path, nLevelsUp) , '/')
    
SOURCEPATH = os.path.abspath(__file__)

print parent_folder(SOURCEPATH,1) #           /media/jwatson/FILEPILE/Python/Snippets
print parent_folder_name_only(SOURCEPATH,1) # Snippets
print parent_folder(SOURCEPATH,2) #           /media/jwatson/FILEPILE/Python
print parent_folder_name_only(SOURCEPATH,2) # Python