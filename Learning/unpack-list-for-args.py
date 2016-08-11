def fourArgFunc(arg1, arg2, arg3, arg4):
    print "Found 4 args:", arg1, arg2, arg3, arg4
    
foo = [1,2,3,4]

fourArgFunc(*foo) # Found 4 args: 1 2 3 4
# Python successfully unpacked list for positional args

fourArgFunc(*[5,6,7,8]) # Found 4 args: 5 6 7 8

fourArgFunc('apple',*[9,10,11]) # Found 4 args: apple 9 10 11

# fourArgFunc(*[12,13] , *[14,15]) # ERROR: invalid syntax
# fourArgFunc(*[12,13] + *[14,15]) # ERROR: invalid syntax
fourArgFunc(*[12,13] + [14,15]) # Found 4 args: 12 13 14 15
fourArgFunc( *([12,13] + [14,15]) ) # Found 4 args: 12 13 14 15