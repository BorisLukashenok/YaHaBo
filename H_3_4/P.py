from itertools import product, chain, combinations

s_im = ["буби", "пики", "трефы", "черви"]
s_rod = ["бубен", "пик", "треф", "червей"]
nominal = list(chain(sorted([str(i) for i in range(2, 11)]), [
               "валет", "дама", "король", "туз"]))
ss = s_rod[s_im.index(input())]
nominal.remove(input())
temp = 0
for value in combinations(product(nominal, s_rod), 3):
    stroka = ", ".join([str(" ".join(i)) for i in value])
    if temp < 10:
        if ss in stroka:
            print(stroka)
            temp += 1            
    else:
        break
