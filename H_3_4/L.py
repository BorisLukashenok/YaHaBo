from itertools import chain

for i, n in enumerate(sorted(chain.from_iterable([chain(input().split(', ')) for i in range(int(input()))])), 1):
    print(f'{i}. {n}')