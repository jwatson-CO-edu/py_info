## This example displays the number of bytes taken by non-directory files in each directory under the starting directory, 
## except that it doesn’t look under any CVS subdirectory:

import os
from os.path import join, getsize

# There might not be a platform-independent way to detect drives.  Will need to set up environment based on the OS running the script

# It appears that if you are looking for all the drives in Windows, then you must try all of the letters of the alphabet, testing if each is a drive
#with
print os.path.isdir("C:/")
# replace C with every letter of the alphabet
# Otherwise I am not sure how to reach drives that are not letter names unless you know them beforehand

# This might work in windows?
## localdrives = [drive for drive in
## win32api.GetLogicalDriveStrings().split('\x00')[:-1] if
## win32file.GetDriveType(drive) in [win32file.DRIVE_FIXED,
## win32file.DRIVE_CDROM, win32file.DRIVE_REMOVABLE]]


for root, dirs, files in os.walk('python/Lib/email'):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
