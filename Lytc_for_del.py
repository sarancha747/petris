import time, curses, threading

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
            countdown_thread = threading.Thread(target=countdown, args=(c_y, c_x, stdscr,))
            countdown_thread.start()
            c_y += 1
        key = stdscr.getch()
        # if key == curses.KEY_DOWN:
        #     E[c_y][c_x] = 0
        #     E[c_y][c_x + 1] = 0
        #     c_y += 1

        if key == curses.KEY_RIGHT:
            E[c_y][c_x] = 0
            E[c_y + 1][c_x] = 0
            c_x += 1
            stdscr.refresh()

        if key == curses.KEY_LEFT:
            E[c_y][c_x + 1] = 0
            E[c_y + 1][c_x + 1] = 0
            c_x -= 1
            stdscr.refresh()

        stdscr.refresh()

    return

def countdown(c_y, c_x, stdscr):
    time.sleep(1)
    E[c_y][c_x] = 0
    E[c_y][c_x + 1] = 0
    global my_timer
    my_timer = 0
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    while True:
        o_block(stdscr)
        # stdscr.clear()

if __name__ == '__main__':
    curses.wrapper(main)
