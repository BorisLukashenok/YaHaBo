a = [
    [int(input()), 'Петя'],
    [int(input()), 'Вася'],
    [int(input()), 'Толя']
]
a = sorted(a, reverse=True)
for i in range(3):
    print(f"{i + 1}. {a[i][1]}")