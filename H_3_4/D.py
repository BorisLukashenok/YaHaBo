from itertools import accumulate

for value in accumulate(input().split(), lambda a, b: a + ' ' + b):
    print(value)
