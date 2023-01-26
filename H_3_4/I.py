from itertools import product

for i, j in product(range(1, num := int(input()) + 1), repeat=2):
    print(i * j, end="\n" if j == num - 1 else " ")