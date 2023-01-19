sa = {}
for i in range(int(input())):
    if not sa.get(k := input(), 0):
        sa[k] = 1
    else:
        sa[k] += 1
count = 0
flag = True
for i in sorted(sa):
    if sa[i] > 1:
        print(f'{i} - {sa[i]}')
        flag = False
if flag:
    print('Однофамильцев нет')
