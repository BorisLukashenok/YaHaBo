from itertools import product

result = input()
print(f'a b c f')
for a, b, c in list(product([0, 1], repeat=3)):       
    print(f'{a} {b} {c} {int(eval(result))}')
