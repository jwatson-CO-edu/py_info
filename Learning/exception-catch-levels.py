foo = { 1:'dog' , 2:'cat' }

def access_with_catch(key):
    try:
        return foo[key]
    except KeyError:
        print " access_with_catch : Caught a KeyError! " # Only this message is printed, error goes no further because
        #                                                  Python assumes you handled it fully when you cauught it!
        
try:
    access_with_catch(3)
except BaseException:
    print "main : error at a deeper level" # This one never shows up, it was caught inside the function