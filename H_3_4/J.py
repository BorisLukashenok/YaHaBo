from itertools import product

print("А Б В")
for i, j, k in product(range(1, n := int(input()) + 1), repeat=3):
    if n - 1 == i + j + k:
        print(i, j, k)
