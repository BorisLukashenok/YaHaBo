from math import comb

n, m = list(map(int, input().split()))
print(comb(n-1, m-1), comb(n, m))
