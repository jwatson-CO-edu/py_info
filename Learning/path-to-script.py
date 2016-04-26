# -*- coding: utf-8 -*-
import os

scriptPath = os.path.abspath(__file__)
print scriptPath # /media/jwatson/FILEPILE/Python/Learning/path-to-script.py
scriptDir, scriptName = os.path.split(scriptPath)
print scriptDir # /media/jwatson/FILEPILE/Python/Learning
print scriptName # path-to-script.py