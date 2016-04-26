# -*- coding: utf-8 -*-

""" URL, Priority Queue: https://en.wikipedia.org/wiki/Priority_queue
A priority queue is an abstract data type which is like a regular queue or stack data structure, 
but where additionally each element has a "priority" associated with it. In a priority queue, an element with 
high priority is served before an element with low priority. If two elements have the same priority, 
they are served according to their order in the queue. """

from Queue import PriorityQueue

q1 = PriorityQueue()
q1.put(10)
q1.put(1)
q1.put(5)
while not q1.empty():
	print q1.get(), # 1 5 10

print

q2 = PriorityQueue()
q2.put( (10,'foo') )
q2.put( ( 1,'bar') )
q2.put( ( 5,'baz') )
while not q2.empty():
	print q2.get(), # (1, 'bar') (5, 'baz') (10, 'foo')

print

q2.put( (10,'foo') )
q2.put( ( 1,'bar') )
q2.put( ( 5,'baz') )
print "There are",len(q2),"items in 'q2'"
while not q2.empty():
	print q2.get()[1], # bar baz foo