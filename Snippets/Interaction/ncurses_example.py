from curses import wrapper

def main( stdscr ):
    # Clear screen
    stdscr.clear()

    stdscr.addstr(0, 0, '10 divided by {} is {}'.format(4, 10/4))

    stdscr.refresh()
    stdscr.getkey()

wrapper( main )