class Rectangle:
    def __init__(self, angle1, angle2):
        self.angle1 = angle1
        self.angle2 = angle2

    def perimeter(self):
        return round(2 * (abs(self.angle1[0] - self.angle2[0]) + abs(self.angle1[1] - self.angle2[1])), 2)

    def area(self):
        return round(abs(self.angle1[0] - self.angle2[0]) * abs(self.angle1[1] - self.angle2[1]), 2)