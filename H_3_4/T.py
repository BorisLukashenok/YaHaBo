# импликация A -> B  not(A) or B
# строгая дизьюнкция A ^ B   not A == B
# эквивалентность это когда равны таблицы истинности F(A) == F(B)
# A -> B ~ C     not (A) or B == C
# A or C ~ not (A -> B) or C     ( A or C ) == (not (not( A ) or B ) or C )

from itertools import product

expres = input()
list_var = sorted(set(i for i in expres.replace(")", ' ').replace(
    "(", ' ').split() if len(i) == 1 and i.isalpha() and i.isupper()))
while '~' in expres or '->' in expres or '^' in expres:
    match expres:
        case _ if '~' in expres:
            expres = ' == '.join([f"({i})" for i in expres.split(' ~ ')])
        case _ if '->' in expres:
            temp = expres.find(' -> ')
            srez = expres[temp - 1: temp + 5]
            rep = f'(not ({srez[0]}) or {srez[-1]})'
            expres = expres.replace(srez, rep)
        case _ if '^' in expres:
            temp = expres.find(' ^ ')
            srez = expres[temp - 1: temp + 4]
            rep = f'(not {srez[0]} == {srez[-1]})'
            expres = expres.replace(srez, rep)

print(f'{" ".join(list_var)} F')
for val in product([0, 1], repeat=len(list_var)):
    print(f'{" ".join(map(str, val))} {int(eval(expres, dict(zip(list_var, val))))}')
