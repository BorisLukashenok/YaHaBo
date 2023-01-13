min = 0
max = 1001
print(a := (min + max) // 2)
while (b := input()) != 'Угадал!':
    if b == 'Больше':
        min = a
    elif b == 'Меньше':
        max = a
    print(a := (min + max) // 2)
    
