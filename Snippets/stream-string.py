import cStringIO

inputStr = \
"""zero
one
two
three
four
five
six
seven
eight
nine"""

bufr = cStringIO.StringIO( inputStr )

def read_two(stream):
    print "'read_two' got", stream.__class__
    for i in xrange(2):
        print stream.readline().rstrip()
        
def read_three(stream):
    print "'read_three' got", stream.__class__
    for i in xrange(3):
        print stream.readline().rstrip()

read_two(bufr)
read_three(bufr)

print "Reading remainder of", bufr.__class__
for i in xrange(6):
    print bufr.readline().rstrip()
    
print bufr.__class__.__name__ #    'StringI'
print ('dog').__class__.__name__ # 'str'
print (3).__class__.__name__ #     'int'
"""
'read_two' got <type 'cStringIO.StringI'>
zero
one
'read_three' got <type 'cStringIO.StringI'>
two   # <-- Stream keeps its place, even when passed between functions
three
four
Reading remainder of <type 'cStringIO.StringI'>
five
six
seven
eight
nine
"""