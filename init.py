from Game import Game
from Size import Size
from GameOverException import GameOverException

size = Size(width=100, height=20)

game = Game(size)

try:
    game.play(0.5)
except GameOverException:
    print('Game over...')