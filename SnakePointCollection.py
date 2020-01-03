from PointCollection import PointCollection


class SnakePointCollection(PointCollection):

    def shift_points(self, current_point):
        new_points = []
        for i in range(1, len(self.points)):
            new_points.append(self.points[i])
        new_points.append(current_point)
        self.points = new_points
        return self.points

    def add_point(self, current_point):
        self.points.append(current_point)
        return self.points
