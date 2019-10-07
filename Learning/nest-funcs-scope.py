def outerfunc():
    outerVar = 1
    def innerfunc():
        global outerVar # ERROR: This is not a global somehow
        outerVar += 1
        print( "innerfunc" , outerVar )
    innerfunc()
    print( "outerfunc" , outerVar )
    
def outerfunc2():
    def innerfunc2():
        outerfunc2.outerVar += 1
        print( "innerfunc" , outerfunc2.outerVar )
    innerfunc2()
    print( "outerfunc" , outerfunc2.outerVar )
outerfunc2.outerVar = 1
    
# outerfunc() # Error!
outerfunc2()