import threading
from queue import Queue
from time import sleep
from time import time
from math import floor


class TimerThread( threading.Thread ):
    """ Continue to do work until the thread is killed """
    
    def __init__( self , Q , workFunc , updateHz , stopToken = None ):
        """ Set up worker and queue management """
        super().__init__()
        self.Q         = Q # --- Parent Queue that holds this thread and all the commands that it will execute
        self.workF     = workFunc # Function to be executed every iteration
        self.period    = 1.0 / updateHz
        self.stopToken = stopToken
        self.killed    = False # Flag for whether anyone has asked this thread to die
        self.count     = 0 # --- DEBUG: Count how many commands were run before dying
        self._DEBUG    = 1 # --- DEBUG: flag
        
    def run( self ):
        """ Execute the work function repeatedly until asked to stop """
        # 0. Initialize the queue with one item
        self.Q.put( time() )
        # 1. Do until you don't
        while 1:
            # 2. Fetch the next item
            item = self.Q.get()
            # 3. Check for the poison pill and stop if found
            if item == self.stopToken:
                break
            # 4. Else execute and repeat
            else:
                # 5. Get the current time, the time elapsed, and the next scheduled time
                t_dif = item - time()
                # 6. If we consumed the token too early, then wait
                if t_dif > 0.0:
                    sleep( t_dif )
                # 7. Calc a time in the future to consume the next work unit, and put a new token
                t_fut = time() + self.period
                self.Q.put( t_fut )
                # 8. Do the work
                self.workF()
                self.count += 1
                
                if self._DEBUG:  print( "Thread executed" , self.count , "times" )

class TimerQueue( Queue ):
    """ Perform work at semi-steady intervals until asked to stop """
    
    def __init__( self , workFunc , updateHz , stopToken = None ):
        """ Set up the queue """
        super().__init__()
        self.workFunc  = workFunc
        self.updateHz  = updateHz
        self.stopToken = stopToken
        self.worker    = None
        self.running   = False
        
    def start( self ):
        """ Start work and run forever """
        self.worker  = TimerThread( Q = self , workFunc = self.workFunc , updateHz = self.updateHz , stopToken = self.stopToken )
        self.running = True
        self.worker.start()
        
    def stop( self ):
        """ Administer the poison pill """
        if ( not self.empty() ) or ( self.is_running() ):
            self.put( self.stopToken )
        self.running = False
        
    def is_running( self ):
        """ Return true if the worker is working, otherwise return false """
        try:
            return self.worker.is_alive()
        except:
            return False
        
if __name__ == "__main__":
    
    # 1. Define a silly work function
    def busy_work():
        print( "The current time is" , time() )
        
    # 2. Create a queue and start it
    q = TimerQueue( workFunc = busy_work , updateHz = 10 )
    q.start()
    
    # 3. Do something else at the same time
    for i in range( 5 ):
        print( "beep" )
        sleep( 1/5.0 )
        
    # 4. Wait for it ...
    sleep( 0.5 )
    q.stop()
    
    print( q.is_running() )
    sleep( 0.5 )
    print( q.is_running() )
    
    
    