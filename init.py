from Game import Game
from Size import Size
from GameOverException import GameOverException

size = Size(width=100, height=20)

game = Game(size)

try:
    game.play(0.5)
except GameOverException:
    print('Game over...')


#
# init_fruits = FruitPointCollection([Position(height // 4, width // 2)])
# init_pos = Position(height // 2, width // 2)
#
# game_map = GameMap(size, init_fruits, init_pos)
#
# draw_game_settings = DrawGameSettings('0', 'F', '#', ' ')
# draw_game = GameDrawer(game_map, draw_game_settings)
#
# game_controller = GameController()
#
# while True:
#     direction = game_controller.determine()
#
#     game_map.move(direction)
#
#     time.sleep(0.25)
#
#     os.system('clear')
#
#     draw_game.draw()
