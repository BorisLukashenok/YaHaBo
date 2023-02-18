import pandas as pd
import numpy as np


def values(func, start, end, step):
    index = np.arange(start, end + step, step)
    return pd.Series([func(i) for i in index], index=index)


def min_extremum(data: pd.Series):
    return data[data == data.min()].index[0]


def max_extremum(data):
    return data[data == data.max()].index[0]


data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
