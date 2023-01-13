a = int(input())
b = int(input())
for i in range(a):
    for j in range(b * i + 1, b * (i + 1) + 1):
        print(f'{j}'.rjust(len(str(a * b)), ' '), end=' ')
    print()
