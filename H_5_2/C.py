class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, obg):
        return round(((self.x - obg.x) ** 2 + (self.y - obg.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x = args[0]
                self.y = args[1]

    def __str__(self) -> str:
        return f'{self.x, self.y}'

    def __repr__(self) -> str:
        return f'PatchedPoint{self.x, self.y}'

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)
first_point = second_point = PatchedPoint((2, -7))
print(first_point, second_point)
first_point += (7, 3)
print(first_point)
print(first_point, second_point, first_point is second_point)
