import pandas as pd
from string import punctuation, digits


def length_stats(text: str):
    lst = sorted(text.translate({ord(i): None for i in punctuation + digits}).lower().split())
    data = {i: len(i) for i in lst}
    pds = pd.Series(data)
    return pds[pds % 2 == 1], pds[pds % 2 == 0]


print(length_stats('Мама мыла раму'))
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))