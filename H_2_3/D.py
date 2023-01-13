a = int(input())
b = int(input())

if a <= b:
    for i in range(a, b + 1):
        print(i, end=' ')
if b < a:
    for i in range(a, b - 1, -1):
        print(i, end=' ')