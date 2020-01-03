from SnakePointCollection import SnakePointCollection
from Point import Point as Position
from Direction import Direction
from BoundException import BoundException
from CutYourselfException import CutYourselfException
import random


class GameMap:

    def __init__(self, size, init_fruits, init_pos):
        self.size = size
        self.fruits = init_fruits
        self.snake = SnakePointCollection([init_pos])
        self.position = init_pos

    '''Calc random position on map and put fruit on it'''
    def add_fruit(self):
        width, height = self.size.get_size()

        x = random.randint(1, width)
        y = random.randint(1, height)
        self.fruits.add(Position(y, x))

    def change_position(self, direction):
        y, x = self.position.coords()
        if direction == Direction.DOWN:
            self.position = Position(y + 1, x)
        elif direction == Direction.UP:
            self.position = Position(y - 1, x)
        elif direction == Direction.LEFT:
            self.position = Position(y, x - 1)
        elif direction == Direction.RIGHT:
            self.position = Position(y, x + 1)

    def move(self, direction):

        width, height = self.size.get_size()

        # Change position
        self.change_position(direction)

        # Current position of snake
        x, y = self.position.coords()

        # Check whether snake is out of boundaries
        if x <= 0 or x >= height - 1 or y <= 0 or y >= width - 1:
            raise BoundException

        # Check whether snake had tried to eat himself
        if self.snake.has_point(self.position):
            raise CutYourselfException

        # Check whether snake is at fruit pos
        if self.fruits.has_point(self.position):
            self.snake.add_point(self.position)
            self.fruits.delete(self.position)
            self.add_fruit()
        else:
            # Shift snake
            self.snake.shift_points(self.position)
