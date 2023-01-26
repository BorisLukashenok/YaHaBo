from itertools import product
a = int(input())
b = int(input())
for i, j in product(range(a), range(1, b + 1)):
    print(f'{j + b * i}'.rjust(len(str(a * b)), ' '),
          end="\n" if j == b else " ")
