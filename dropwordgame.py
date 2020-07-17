import sys, os
import curses
import random
import time
from curses import textpad


def draw_menu(stdscr):
    k = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        # 삽입
        # word random choice
        f = open("./wordlist.txt", 'r')
        word_list = f.read().splitlines()
        count = len(word_list)
        i = 0

        # 만든 박스---------------------
        sh, sw = stdscr.getmaxyx()
        box = [[3, 3], [sh - 8, sw - 5]]
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

        editwin_uly = (int(stdscr.getmaxyx()[0] * 0.7 + 1))
        editwin_ulx = (int(stdscr.getbegyx()[1]))
        editwin_lry = (int(stdscr.getmaxyx()[0] - 1))
        editwin_lrx = (int(stdscr.getmaxyx()[1] - 2))
        textpad.rectangle(stdscr, editwin_uly, editwin_ulx, editwin_lry, editwin_lrx)

        for i in range(10):
            show_list = word_list[i:count:100]
            x = random.randrange(int(width / 4), int(width / 4 * 3))
            y = random.randrange(int(height / 4), int(height / 4 * 3))
            stdscr.addstr(y, x, show_list[i])
        time.sleep(6)
        stdscr.refresh()
        continue

        # input창이 안 먹음
        # stdscr = curses.initscr()
        # window = stdscr.subwin(23, 79, 0, 0)
        # window.refresh()
        # window.addstr(20, 45, "This is my line of text")
        # window.addstr(4, 20, "What happened? ")
        # window.refresh()
        #
        # mykey = window.getkey(5, 20)
        # mystr = window.getstr(5, 20)
        # # window.addstr (7,1, "Key data should be here: ")
        # # window.addstr (7,33, mykey)
        # while True:
        #     window.addstr(7, 10, "Str data should be here: ")
        #     window.addstr(8, 33, mystr)
        #     window.refresh()

        # ----------만든 박스-----------------
        # word random choice

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()