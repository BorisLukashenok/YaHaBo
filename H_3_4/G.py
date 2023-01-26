from itertools import combinations

for a, b in combinations([input() for i in range(int(input()))], 2):
    print(f'{a} - {b}')