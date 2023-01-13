a = int(input())
b = int(input())
for i in range(1, a + 1):
    for j in range(i, b * a + 1, a):
        print(f'{j}'.rjust(len(str(a * b)), ' '), end=' ')
    print()
