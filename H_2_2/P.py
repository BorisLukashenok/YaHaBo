a = [
    [int(input()), 'Петя'],
    [int(input()), 'Вася'],
    [int(input()), 'Толя']
]
a = sorted(a, reverse=True)
print(a[0][1].center(24, ' '))
print(a[1][1].center(8, ' '))
print(a[2][1].rjust(22, ' '))
print('II'.center(8, " "), 'I'.center(8, " "), 'III'.center(8, " "), sep='')
