import numpy as np


def rotate(matrix, angle):
    return np.rot90(matrix, -angle / 90)

print(rotate(np.arange(12).reshape(3, 4), 90))
print(rotate(np.arange(12).reshape(3, 4), 270))