from itertools import permutations, chain

print('\n'.join(' '.join(j) for j in sorted(permutations(chain.from_iterable(
    [chain(input().split(', ')) for i in range(int(input()))]), 3))))
