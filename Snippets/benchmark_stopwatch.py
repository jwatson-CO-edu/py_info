# -*- coding: utf-8 -*-
from timeit import default_timer as timer # URL, Benchmarking: http://stackoverflow.com/a/25823885

class Stopwatch(object):
    """ Singleton objecy for benchmarking """
    strtTime = 0
    stopTime = 0
    @staticmethod
    def start():
        Stopwatch.strtTime = timer()
    @staticmethod
    def stop():
        Stopwatch.stopTime = timer()
    @staticmethod
    def elapsed():
        return Stopwatch.stopTime - Stopwatch.strtTime