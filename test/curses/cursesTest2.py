import curses
from collections import defaultdict

stdscr=curses.initscr()

line= '+' + ('+------' * 4 + '+')[1:]
separator = defaultdict(lambda: line)
stdscr.addstr(separator)

stdscr.getkey()