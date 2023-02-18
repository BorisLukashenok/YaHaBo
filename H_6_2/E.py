import pandas as pd


def get_long(df: pd.DataFrame, min_length=5):
    return df[df >= min_length]


data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
filtered = get_long(data)
print(data)
print(filtered)
