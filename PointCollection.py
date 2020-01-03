class PointCollection:

    def __init__(self, init_points=[] ):
        self.points = init_points

    def add(self, point):
        self.points.append(point)

    def get_points(self):
        return self.points

    def has_point(self, search_point):
        for point in self.points:
            if point.coords() == search_point.coords():
                return True
        return False

    def delete(self, point_to_delete):
        self.points = list( filter(lambda point: point.coords() != point_to_delete.coords(),
                                    self.points
                                  )
                          )