from math import log, cos, sin, pi, e

x = float(input())
print(log(x ** (3 / 16), 32) + x ** cos(pi * x / (2 * e)) - sin(x / pi) ** 2)
