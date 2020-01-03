from Point import Point as Position
from FruitPointCollection import FruitPointCollection


def get_init_fruits(size):
    width,height = size.get_size()
    return FruitPointCollection([Position(height // 4, width // 2)])


def get_init_pos(size):
    width, height = size.get_size()
    return Position(height // 2, width // 2)