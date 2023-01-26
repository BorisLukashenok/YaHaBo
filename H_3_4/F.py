from itertools import product, chain

nominal = chain([str(i) for i in range(2, 11)], ['валет', 'дама', 'король', 'туз'])
mast = ['пик', 'треф', 'бубен', 'червей']
mast.remove(input())
for i, j in product(nominal, mast):
    print(i, j)

