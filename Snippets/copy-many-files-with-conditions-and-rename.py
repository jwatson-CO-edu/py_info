# -*- coding: utf-8 -*-
"""
ycb-scraper.py , Built on Spyder for Python 2.7
James Watson, 2016 March
Scrape files fitting a certain description from the YCB dataset and put them in the specified place

"""
# == Init Environment ==

# ~ PATH Changes ~ 
def localize(): # For some reason this is needed in Windows 10 Spyder (Py 2.7)
    """ Add the current directory to Python path if it is not already there """
    from sys import path # I know it is bad style to load modules in function
    import os.path as os_path
    containerDir = os_path.dirname(__file__)
    if containerDir not in path:
        path.append( containerDir )

localize() # You can now load local modules!

# ~ Standard Libraries ~
import math
from math import sqrt, ceil, sin, cos, tan, atan2, radians
from os import linesep
import os
import shutil
from Queue import PriorityQueue
# ~ Special Libraries ~
import matplotlib.pyplot as plt
import numpy as np
# ~~ Constants , Shortcuts , Aliases ~~
EPSILON = 1e-7
infty = 1e309 # URL: http://stackoverflow.com/questions/1628026/python-infinity-any-caveats#comment31860436_1628026
endl = linesep

# ~ Helper Functions ~

def eq(op1, op2):
    """ Return true if op1 and op2 are close enough """
    return abs(op1 - op2) <= EPSILON
    
def sep(title = ""):
    """ Print a separating title card for debug """
    LINE = '======'
    print LINE + ' ' + title + ' ' + LINE

# == End Init ==

def abbreviate_name(YCBdirName):
    """ Create an abbreviated version of the YCB overlong filenames """
    ABBREVLEN = 4
    charCount = 0
    rtnStr = ''
    if '_' in YCBdirName: # in name has underscores
        for char in YCBdirName:
            if char != '_':
                if charCount < ABBREVLEN:
                    if charCount == 0:
                        rtnStr += char.upper()
                    else:
                        rtnStr += char
                charCount += 1
            else:
                charCount = 0
    else: # else no underscore, name is probably short
        rtnStr = YCBdirName
    return rtnStr

def parent_folder(item, nLevelsUp):
    """ Return the containing directory that is 'nLevelsUp' from 'item' """
    if nLevelsUp == 0:
        return item
    else:
        return parent_folder(os.path.dirname(item), nLevelsUp-1)
        
def last_X_to_end(longStr,charX):
    """ Return the portion of 'longStr' that is occurs after the last instance of 'charX' is present, otherwise return 'longStr' """
    rtnStr = ''
    charDex = -1
    while longStr[charDex] != charX and charDex >= -len(longStr):
        rtnStr = longStr[charDex] + rtnStr
        charDex -= 1
    return rtnStr

copyList = []

# URL, Traversing Directories: http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
srchDir = '/home/jwatson/utah_regrasp/ycb' 
srchDirFound = os.path.isdir(srchDir)  # http://stackoverflow.com/a/3204819/893511
print "Found search directory:",srchDirFound,endl,srchDir
copyDir = '/home/jwatson/utah_regrasp/mesh_tests/models/spam/utah_regrasp' 
copyDirFound = os.path.isdir(copyDir)
print "Found copy directory:",copyDirFound,endl,copyDir

if srchDirFound and copyDirFound:
    for dirName, subdirList, fileList in os.walk(srchDir): #, topdown=False):
        if dirName != srchDir: # ignore the search directory
            print dirName, subdirList, fileList # print where we are
            for fname in fileList: # for every file in this directory
                if fname[-3:] == 'stl': # if the file is the type we want: STL
                    print '\t{}'.format(fname),' --in--> ',dirName # print that we found it
                    fullName = os.path.join(dirName, fname) # build the full path to the file
                    if 'tsdf' in fname: # separate by Poisson or TSDF, I don't know yet what the difference is
                        fldr = 'tsdf_stl/'
                    elif 'poisson' in fname:
                        fldr = 'pssn_stl/'
                    else:
                        fldr = ''
                    # Create a new, short, descriptive filename to copy to 
                    copyName = os.path.join(copyDir, fldr + abbreviate_name(last_X_to_end(parent_folder(dirName, 1),'/')) + '.stl')
                    copyList.append( (fullName , copyName) ) # build a list of copy operations to perform
                         
    for srcDestPair in copyList: # Execute the list of copy operations
        print "Copying",srcDestPair[0],"to..."
        shutil.copy2( srcDestPair[0], srcDestPair[1] )
        print "\t",srcDestPair[1]
else:
    print "Either search or copy directory was not found"