class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column


    def __str__(self):
        return f"Point: {self.row} {self.column}"

    def set(self, row, column):
        self.row = row
        self.column = column

    def coords(self):
        return self.row, self.column
