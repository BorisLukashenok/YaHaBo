sa = dict()
for i in range(int(input())):
    b = input().split()
    sa[b[0]] = b[1:]
kasha = input()
flag = True
for k, v in sorted(sa.items()):
    if kasha in v:
        print(k)
        flag = False
if flag:
    print('Таких нет')
