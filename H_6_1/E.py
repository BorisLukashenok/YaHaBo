from math import dist, cos, sin

deka = map(float, input().split())
p_x, p_y = map(float, input().split())
pole = (p_x * cos(p_y), p_x * sin(p_y))
print(dist(deka, pole))
