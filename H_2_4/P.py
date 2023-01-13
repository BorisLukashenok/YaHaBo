a = int(input())
weight = int(input())
for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(f'{i * j:^{weight}}', end="|" if j < a else "\n")
    if i < a:
        print('-' * (a * weight + a - 1))
