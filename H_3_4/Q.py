from itertools import product, chain, combinations

s_im = ["буби", "пики", "трефы", "черви"]
s_rod = ["бубен", "пик", "треф", "червей"]
nominal = list(chain([str(i) for i in range(2, 11)], [
               "валет", "дама", "король", "туз"]))
ss = s_rod[s_im.index(input())]
sn = input()
pred = input()
coloda = list(", ".join(j) for j in combinations(
    [' '.join(i) for i in product(nominal, s_rod)], 3))
for val in coloda[coloda.index(pred) + 1:]:
    if ss in val and sn not in val:
        print(val)
        break
