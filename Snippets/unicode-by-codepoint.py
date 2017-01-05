from random import randrange

#print u'\u25d0'
print unichr(9675) , unichr(9684) , unichr(9681) , unichr(9685) , unichr(9679)
print unichr(9474) , unichr(9472) , unichr(9585) , unichr(9586) # Print decimal codepoints
# Print some arrows
print unichr(0x2190) , unichr(0x2191) , unichr(0x2192) , unichr(0x2193) , unichr(0x2196) , unichr(0x2197) , unichr(0x2198) , unichr(0x2199) # hex codepoints

for i in xrange( 500 ):
    codepoint = randrange( 2**16 )
    print codepoint , unichr( codepoint ) , '||' ,
    if i % 10 == 0:
        print
print
    
# print unichr( 2**16 - 20  )