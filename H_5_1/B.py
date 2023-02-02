class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, obg):
        return round(((self.x - obg.x) ** 2 + (self.y - obg.y) ** 2) ** 0.5, 2)