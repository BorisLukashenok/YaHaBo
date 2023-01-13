a = int(input())
b = int(input())
weight = len(str(a * b))
for i in range(a):
    for j in range(1, b + 1):
        if j % 2:
            ot = i + 1
        else:
            ot = -i
        print(f'{(j // 2) * 2 * a + ot}'.rjust(weight, ' '), end=' ')
    print()
