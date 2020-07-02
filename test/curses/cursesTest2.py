#!/usr/bin/env python3
import curses
import time
class CursesHandle:
    def __init__(self):
        '''设置字符串输出位置x与y'''
        self.x = 0
        self.y = 0
        self.stdscr = None

    def __enter__(self):
        '''with使用，初始化curses并设置环境，start_color()、init_pair设置文字与背景颜色'''
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        self.stdscr.nodelay(1)
        return self

    def __exit__(self, exc_ty, exc_val, tb):
        '''with使用，退出时还原环境'''
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()
        self.stdscr = None

    def display_info(self, words, color=1, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        '''打印words字符串，color为1绿2红，在环境里已设置'''
        if self.stdscr is None:
            raise Exception('ERROR: Not self.stdscr exist!')
        self.stdscr.addstr(y, x, words, curses.color_pair(color))
        self.stdscr.refresh()

    def get_input_and_continue(self):
        '''设置中断，等待输入后恢复'''
        if self.stdscr is None:
            raise Exception('ERROR: Not self.stdscr exist!')
        self.stdscr.nodelay(0)
        ch = self.stdscr.getch()
        self.stdscr.nodelay(1)

    def get_input_and_exit(self):
        '''当输入字符为q后退出'''
        if self.stdscr is None:
            raise Exception('ERROR: Not self.stdscr exist!')
        ch = self.stdscr.getch()
        if ch == ord('q'):
            exit(0)

if __name__ == '__main__':
    num = 1
    with CursesHandle() as cur:
        cur.display_info('输入任意值开始！')
        cur.get_input_and_continue()
        while num < 10:
            cur.display_info(str(num), x=10, y=10)
            num+=1
            time.sleep(1)