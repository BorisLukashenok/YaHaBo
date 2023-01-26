from itertools import product

expres = input()
list_var = sorted(set(i for i in expres.split() if len(i) == 1))
print(f'{" ".join(list_var)} F')
for val in product([0, 1], repeat=len(list_var)):
    print(f'{" ".join(map(str, val))} {int(eval(expres, dict(zip(list_var, val))))}')
