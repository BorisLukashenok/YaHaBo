import numpy as np


def make_board(n: int):
    return np.array([[not (i + j) % 2 for i in range(n)] for j in range(n)], dtype=np.int8)