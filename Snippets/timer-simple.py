import time

def elapsed_w_msg( msg = "Elapsed:" ):
    """ Return the time elapsed and print with a msg """
    if elapsed_w_msg.lastTime == None:
        print msg , "Timer started!"
        elapsed_w_msg.lastTime = time.time()
    else:
        elapsed = time.time() - elapsed_w_msg.lastTime
        hours = int( elapsed / elapsed_w_msg.s_in_hr )
        elapsed = elapsed % elapsed_w_msg.s_in_hr
        mins = int( elapsed / elapsed_w_msg.s_in_mn )
        elapsed = elapsed % elapsed_w_msg.s_in_mn 
        print msg , hours , "hrs" , mins , "min" , elapsed , "sec"
        elapsed_w_msg.lastTime = time.time()
elapsed_w_msg.lastTime = None
elapsed_w_msg.s_in_hr = 60 * 60
elapsed_w_msg.s_in_mn = 60