a = int(input())
b = int(input())

flag = True
for i in range(a):
    if flag:
        ot = b * i + 1
        do = b * (i + 1) + 1
        step = 1
    else:
        ot = b * (i + 1)
        do = b * i
        step = -1
    for j in range(ot, do, step):
        print(f'{j}'.rjust(len(str(a * b)), ' '), end=' ')
    print()
    flag = not flag
