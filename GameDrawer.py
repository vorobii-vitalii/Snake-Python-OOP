from Point import Point as Position


class GameDrawer:

    def __init__(self, game_map, draw_settings):
        self.game_map = game_map
        self.draw_settings = draw_settings

    def draw(self):
        width, height = self.game_map.size.get_size()
        for i in range(height + 1):
            for j in range(width + 1):
                pos = Position(i, j)
                if i == 0 or i == height or j == 0 or j == width:
                    print(self.draw_settings.bound_char, end='')
                elif self.game_map.snake.has_point(pos):
                    print(self.draw_settings.snake_char, end='')
                elif self.game_map.fruits.has_point(pos):
                    print(self.draw_settings.fruit_char, end='')
                else:
                    print(self.draw_settings.empty_char, end='')
            print()
