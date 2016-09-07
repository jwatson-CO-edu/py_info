def reverser(*args,**kwargs):
    if 'rev' in kwargs and kwargs['rev']:
        args = args[::-1] 
    for arg in args:
        print arg,
    print
    
reverser(1,2,3)
reverser(1,2,3,rev=1)