from itertools import permutations

print('\n'.join(', '.join(j) for j in sorted(permutations([input() for i in range(int(input()))]))))