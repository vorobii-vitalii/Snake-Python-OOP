class Size:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_size(self):
        return self.width,self.height

    def __str__(self):
        return f"Size {self.width}x{self.height}"