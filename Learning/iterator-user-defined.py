# URL, Build your own iterator: http://anandology.com/python-practice-book/iterators.html

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
        
for i in yrange(4):
    print i ,
print
# 0 1 2 3