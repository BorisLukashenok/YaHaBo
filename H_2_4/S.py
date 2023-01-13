n = int(input())
t = 1
if n > 18:
    t = 2
for i in range(n):
    for j in range(n):
        value = n - max(i, j, n - 1 - i, n - 1 - j)
        print(f'{value:^{t}}', end=" ")
    print()
