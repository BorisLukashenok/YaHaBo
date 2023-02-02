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


point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
