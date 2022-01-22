import curses
import traceback
import datetime
import time

try:
    # -- Initialize --
    stdscr = curses.initscr()   # initialize curses screen
    curses.noecho()             # turn off auto echoing of keypress on to screen
    curses.cbreak()             # enter break mode where pressing Enter key
                                #  after keystroke is not required for it to register
    stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc
    stdscr.nodelay(1)

    # -- Perform an action with Screen --
    stdscr.border(0)
    stdscr.addstr(5, 5, 'Hello from Curses!', curses.A_BOLD)
    stdscr.addstr(6, 5, 'Press q to close this screen', curses.A_NORMAL)

    while True:
        # stay in this loop till the user presses 'q'
        #stdscr.addstr(7, 5, 'zztop',curses.A_NORMAL)
        ti = str((datetime.datetime.now().time()))
        stdscr.addstr(8, 5, 'Time: '+ ti, curses.A_NORMAL)
        
        stdscr.refresh()
        stdscr.timeout(3000)

        key = stdscr.getch()
        if key == ord('q'):
            break



    # -- End of user code --

except:
    traceback.print_exc()     # print trace back log of the error

finally:
    # --- Cleanup on exit ---
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()