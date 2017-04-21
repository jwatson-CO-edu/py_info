#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

"""
RESULT: 'sys.argv' is a list of arguments that the script was called with at the terminal , with the first argument always being the script
        name. On some systems the first argument is the full path to the script
"""

import sys

if __name__ == "__main__":
    # URL , get arguments from the terminal: http://stackoverflow.com/a/1009879/7186022 , https://docs.python.org/2/library/sys.html
    print sys.argv
    print sys.argv[1:] # These are probably the ones you care about
    
"""
python args-command-line.py arg1 arg2 arg3 ---> ['args-command-line.py', 'arg1', 'arg2', 'arg3']
                                                ['arg1', 'arg2', 'arg3']
"""