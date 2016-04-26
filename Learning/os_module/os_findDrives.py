## os_findDrives.py
## James Watson, March 2009
## In Windows, find all the drives specified by a capital letter

import os

# Use the 'os' module to detect operating system and choose platform-specific methods
if 'Windows' in os.environ['OS']:
    print "In Windows"
    print os.environ['OS']

# ord([char]): Given a string of length one, return an integer representing the Unicode code point of 
#the character when the argument is a unicode object, or the value of the byte when the argument is 
#an 8-bit string

def window_drives():
    volumes = []
    # The following segment is for Windows, finds only drives named with uppercase char
    for i in range(ord('a'), ord('z')+1): # iterate over Unicode #s for a-z
        drive = chr(i).upper() + ":/"
        if os.path.isdir(drive): # test if drive letter is a valid directory
            volumes.append(drive)
    return volumes
    
print window_drives()