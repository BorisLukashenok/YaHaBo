import numpy as np


def snake(m, n, direction='H'):
    if direction == 'H':
        a = np.arange(1, m * n + 1, dtype=np.int16).reshape(n, m)
        for i in range(1, n, 2):
            a[i] = a[i][:: -1]
    else:
        a = np.arange(1, m * n + 1, dtype=np.int16).reshape(m, n).transpose()
        for i in range(1, m, 2):
            a[:, i] = a[:, i][:: -1]
    return a


print(snake(5, 3))
