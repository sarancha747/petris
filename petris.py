import time
import curses
import threading
import random

E = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ]
my_timer = 0
starter = 0


def matrix(stdscr):
    x = 0
    y = 0
    for i in range(len(E)):
        # clear()
        # print(E[row])
        for j in range(len(E[i])):
            stdscr.addstr(y, x, str(E[i][j]))
            if x > 8:
                x = 0
                break
            x += 1
        y += 1


def o_block(stdscr):
    c_x = 0
    c_y = 0
    f_type = 'o_block'
    orientation = None
    while True:
        E[c_y][c_x] = 1
        E[c_y][c_x + 1] = 1
        E[c_y + 1][c_x + 1] = 1
        E[c_y + 1][c_x] = 1
        matrix(stdscr)
        stdscr.refresh()
        global my_timer
        if c_y + 1 == 19 or E[c_y + 2][c_x] == 1 or E[c_y + 2][c_x + 1] == 1:
            break
        if my_timer == 0:
            my_timer = 1
            countdown_thread = threading.Thread(target=countdown, args=(c_y, c_x, f_type, orientation, stdscr,))
            countdown_thread.start()
            if starter == 1:
                c_y += 1
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            E[c_y][c_x] = 0
            E[c_y][c_x + 1] = 0
            c_y += 1
        if key == curses.KEY_RIGHT and c_x != 8 and E[c_y][c_x + 2] != 1 and E[c_y + 1][c_x + 2] != 1:
            E[c_y][c_x] = 0
            E[c_y + 1][c_x] = 0
            c_x += 1
            stdscr.refresh()
        if key == curses.KEY_LEFT and c_x != 0 and E[c_y][c_x - 1] != 1 and E[c_y + 1][c_x - 1] != 1:
            E[c_y][c_x + 1] = 0
            E[c_y + 1][c_x + 1] = 0
            c_x -= 1
            stdscr.refresh()
        stdscr.refresh()

    return


def l_block(stdscr):
    c_x = 0
    c_y = 0
    f_type = 'l_block'
    orientation = 1
    while True:
        if orientation == 1:
            E[c_y][c_x] = 1
            E[c_y][c_x + 1] = 1
            E[c_y][c_x + 2] = 1
            E[c_y][c_x + 3] = 1
            matrix(stdscr)
            stdscr.refresh()
            global my_timer
            if c_y == 19 or E[c_y + 1][c_x] == 1 or E[c_y + 1][c_x + 1] == 1 or E[c_y + 1][c_x + 2] == 1 or E[c_y + 1][
                c_x + 3] == 1:
                break
            if my_timer == 0:
                my_timer = 1
                countdown_thread = threading.Thread(target=countdown, args=(c_y, c_x, f_type, orientation, stdscr,))
                countdown_thread.start()
                if starter == 1:
                    c_y += 1
            key = stdscr.getch()
            if key == curses.KEY_UP and c_y <= 16 and E[c_y + 3][c_x] != 1 and E[c_y + 2][c_x] != 1 and E[c_y + 1][
                c_x] != 1:
                orientation = 0
                E[c_y][c_x] = 0
                E[c_y][c_x + 1] = 0
                E[c_y][c_x + 2] = 0
                E[c_y][c_x + 3] = 0
            if key == curses.KEY_DOWN:
                E[c_y][c_x] = 0
                E[c_y][c_x + 1] = 0
                E[c_y][c_x + 2] = 0
                E[c_y][c_x + 3] = 0
                c_y += 1
            if key == curses.KEY_RIGHT and c_x != 6 and E[c_y][c_x + 4] != 1:
                E[c_y][c_x] = 0
                c_x += 1
                stdscr.refresh()
            if key == curses.KEY_LEFT and c_x != 0 and E[c_y][c_x - 1] != 1:
                E[c_y][c_x + 3] = 0
                c_x -= 1
                stdscr.refresh()
        else:
            E[c_y][c_x] = 1
            E[c_y + 1][c_x] = 1
            E[c_y + 2][c_x] = 1
            E[c_y + 3][c_x] = 1
            matrix(stdscr)
            stdscr.refresh()
            # global my_timer
            if c_y == 16 or E[c_y + 4][c_x] == 1:
                break
            if my_timer == 0:
                my_timer = 1
                countdown_thread = threading.Thread(target=countdown, args=(c_y, c_x, f_type, orientation, stdscr,))
                countdown_thread.start()
                if starter == 1:
                    c_y += 1
            key = stdscr.getch()
            if key == curses.KEY_UP:
                orientation = 1
                E[c_y][c_x] = 0
                E[c_y + 1][c_x] = 0
                E[c_y + 2][c_x] = 0
                E[c_y + 3][c_x] = 0
                continue
            if key == curses.KEY_DOWN and c_x <= 6:
                E[c_y][c_x] = 0
                c_y += 1
                stdscr.refresh()
            if key == curses.KEY_RIGHT and c_x != 9 and E[c_y][c_x + 1] != 1 and E[c_y + 1][c_x + 1] != 1 and \
                    E[c_y + 2][c_x + 1] != 1 and E[c_y + 3][c_x + 1] != 1:
                E[c_y][c_x] = 0
                E[c_y + 1][c_x] = 0
                E[c_y + 2][c_x] = 0
                E[c_y + 3][c_x] = 0
                c_x += 1
                stdscr.refresh()
            if key == curses.KEY_LEFT and c_x != 0 and E[c_y][c_x - 1] != 1 and E[c_y + 1][c_x - 1] != 1 and E[c_y + 2][
                c_x - 1] != 1 and E[c_y + 3][c_x - 1] != 1:
                E[c_y][c_x] = 0
                E[c_y + 1][c_x] = 0
                E[c_y + 2][c_x] = 0
                E[c_y + 3][c_x] = 0
                c_x -= 1
                stdscr.refresh()

    #     stdscr.refresh()
    #
    # return


def countdown(c_y, c_x, f_type, orientation, stdscr):
    if f_type == 'o_block':
        E[c_y][c_x] = 0
        E[c_y][c_x + 1] = 0
        time.sleep(1)
        global starter
        starter = 1
        global my_timer
        my_timer = 0
        stdscr.refresh()
    if f_type == 'l_block':
        if orientation == 1:
            E[c_y][c_x] = 0
            E[c_y][c_x + 1] = 0
            E[c_y][c_x + 2] = 0
            E[c_y][c_x + 3] = 0
            time.sleep(1)
            starter = 1
            my_timer = 0
            stdscr.refresh()
        if orientation == 0:
            E[c_y][c_x] = 0
            time.sleep(1)
            starter = 1
            my_timer = 0
            stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    number_list = [1, 2]
    while True:
        # block_list = [o_block(stdscr), l_block(stdscr)]
        # print(random.choice(block_list))  # block_list)
        block_type = random.randint(1, 2)
        l_block(stdscr)
        # if block_type == 1:
        #     o_block(stdscr)
        # else:
        #     l_block(stdscr)


if __name__ == '__main__':
    curses.wrapper(main)
