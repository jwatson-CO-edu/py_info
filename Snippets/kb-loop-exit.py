from time import sleep

while( 1 ):
    try:
        sleep( 0.25 )
        print "Everything is fiiiiine ..."
    except KeyboardInterrupt:
        print "USE HAS PRESSED [CTRL]+[C] !!!"
        break