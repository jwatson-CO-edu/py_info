# iterator_generator.py
# James Watson, October 2010
# An example of iterators and generators in Python
# Uses information from "Tutorial on Python Iterators and Generators" by Norman Matloff

# iterator example; uses Fibonacci numbers, so common in computer
# science examples: f_n = f_{n-1} + f_{n-2}, with f_0 = f_1 = 1

class fibnum:
    def __init__(self):
        self.fn2 = 1 # "f_{n-2}"
        self.fn1 = 1 # "f_{n-1}"
    def next(self): # next() is the heart of any iterator
        # note the use of the following tuple to not only save lines of
        # code but also to insure that only the old values of self.fn1 and
        # self.fn2 are used in assigning the new values
        (self.fn1, self.fn2, oldfn2) = (self.fn1 + self.fn2, self.fn1, self.fn2)
        return oldfn2
    def __iter__(self):
        return self

def try_fibnum():
    f = fibnum()
    for i in f:
        print i
        if i > 20: break

# try_fibnum() # try the fibonacci iterator