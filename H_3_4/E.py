from itertools import chain

for i, n in enumerate(sorted(chain(input().split(', '), input().split(', '), input().split(', '))), 1):
    print(f'{i}. {n}')
