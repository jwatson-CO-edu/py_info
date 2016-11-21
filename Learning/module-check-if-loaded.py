import sys

if "ResearchEnv" not in sys.modules: 
   import os
   EPSILON = 1e-7
   infty = 1e309 # URL: http://stackoverflow.com/questions/1628026/python-infinity-any-caveats#comment31860436_1628026
   endl = os.linesep
   DISPLAYPLACES = 5 # Display 5 decimal places by default
   
print EPSILON