#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

"""
URL, Intro to Multithreading: https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b

RESULT: 
"""

"""
~~ Process -vs- Thread ~~

A process is an instance of program (e.g. Jupyter notebook, Python interpreter). Processes spawn threads (sub-processes) to handle subtasks 
like reading keystrokes, loading HTML pages, saving files. Threads live inside processes and share the same memory space.
* Threads are like mini-processes that live inside a process
* They share memory space and efficiently read and write to the same variables
* Two threads cannot execute code simultaneously in the same python program (although there are workarounds*)


~~ CPU vs Core ~~

The CPU, or processor, manages the fundamental computational work of the computer. CPUs have one or more cores, allowing the CPU 
to execute code simultaneously.


~~ Python’s GIL problem ~~

CPython (the standard python implementation) has something called the GIL (Global Interpreter Lock), 
which prevent two threads from executing simultaneously in the same program. There are workarounds, however, and libraries like Numpy bypass 
this limitation by running external code in C.

~ When to use threads vs processes? ~
* Processes speed up Python operations that are CPU intensive because they benefit from multiple cores and avoid the GIL.
* Threads are best for IO tasks or tasks involving external systems because threads can combine their work more efficiently. 
  Processes need to pickle their results to combine them which takes time.  Threads provide no benefit in python for 
  CPU intensive tasks because of the GIL.
"""