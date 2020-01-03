import curses
from Direction import Direction


def main(stdscr):
    stdscr.nodelay(True)
    return stdscr.getch()


class GameController:

    def __init__(self, direction):
        self.direction = direction

    def determine(self):
        key = curses.wrapper(main)
        if key == 119:
            self.direction = Direction.UP
        elif key == 115:
            self.direction = Direction.DOWN
        elif key == 97:
            self.direction = Direction.LEFT
        elif key == 100:
            self.direction = Direction.RIGHT
        return self.direction
