from default import get_init_fruits, get_init_pos
from Direction import Direction
from GameMap import GameMap
from GameController import GameController
from DrawGameSettings import DrawGameSettings
from GameDrawer import GameDrawer
import os, time
from CutYourselfException import CutYourselfException
from BoundException import BoundException
from GameOverException import GameOverException


class Game:

    def __init__(self, size, init_fruits=None, init_pos=None, draw_settings=None, default_direction=Direction.LEFT):
        self.size = size

        self.game_controller = GameController(default_direction)

        if init_fruits is None:
            init_fruits = get_init_fruits(size)

        if init_pos is None:
            init_pos = get_init_pos(size)

        self.game_map = GameMap(size, init_fruits, init_pos)

        if draw_settings is None:
            draw_settings = DrawGameSettings()

        self.game_drawer = GameDrawer(self.game_map, draw_settings)

    def play(self, delay=0.4):

        while True:
            direction = self.game_controller.determine()

            try:
                self.game_map.move(direction)
            except CutYourselfException:
                raise GameOverException
            except BoundException:
                raise GameOverException

            time.sleep(delay)

            os.system('clear')

            self.game_drawer.draw()
