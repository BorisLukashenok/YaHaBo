class Rectangle:

    def __init__(self, angle1, angle2):
        self.angle = (min(angle1[0], angle2[0]), max(angle1[1], angle2[1]))
        self.w = round(max(angle1[0], angle2[0]) -
                       min(angle1[0], angle2[0]), 2)
        self.h = round(max(angle1[1], angle2[1]) -
                       min(angle1[1], angle2[1]), 2)

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

    def resize(self, dx, dy):
        self.w = dx
        self.h = dy


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
print()
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
