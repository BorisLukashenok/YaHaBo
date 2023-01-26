from itertools import count

s, e, p = input().split()
for value in count(float(s), float(p)):
    if value <= float(e):
        print(round(value, 2))
    else:
        break
