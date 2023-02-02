class Rectangle:

    def __init__(self, angle1, angle2):
        self.angle = (min(angle1[0], angle2[0]), max(angle1[1], angle2[1]))
        self.w = round(max(angle1[0], angle2[0]) -
                       min(angle1[0], angle2[0]), 2)
        self.h = round(max(angle1[1], angle2[1]) -
                       min(angle1[1], angle2[1]), 2)
        self.c = (round(self.angle[0] + self.w / 2, 2),
                  round(self.angle[1] - self.h / 2, 2))

    def perimeter(self):
        return round(2 * self.h + 2 * self.w, 2)

    def area(self):
        return round(self.h * self.w, 2)

    def get_pos(self):
        return self.angle

    def get_size(self):
        return self.w, self.h

    def move(self, dx, dy):
        self.angle = (round(self.angle[0] + dx, 2),
                      round(self.angle[1] + dy, 2))
        self.c = (round(self.angle[0] + self.w / 2, 2),
                  round(self.angle[1] - self.h / 2, 2))

    def resize(self, dx, dy):
        self.w = dx
        self.h = dy
        self.c = (round(self.angle[0] + self.w / 2, 2),
                  round(self.angle[1] - self.h / 2, 2))

    def turn(self):
        self.angle = (round(self.c[0] - self.h / 2, 2),
                      round(self.c[1] + self.w / 2, 2))
        self.w, self.h = self.h, self.w

    def scale(self, factor):
        self.h *= factor
        self.w *= factor
        self.angle = (round(self.c[0] - self.w / 2, 2),
                      round(self.c[1] + self.h / 2, 2))


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')
