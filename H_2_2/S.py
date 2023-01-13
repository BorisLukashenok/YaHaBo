dang = 'Опасность! Покиньте зону как можно скорее!'
free = 'Зона безопасна. Продолжайте работу.'
x = float(input())
y = float(input())
flag = True
if (x ** 2 + y ** 2) ** 0.5 > 10:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
else:
    if y >= 0:
        if x >= 0:
            if (x ** 2 + y ** 2) ** 0.5 <= 5:
                flag = not flag
        else:
            if y <= 5 and y <= ((5 * x) + 35) / 3:
                flag = not flag
    else:
        if y <= (0.25 * (x ** 2)) + (0.5 * x) + 8.75:
            flag = not flag
if flag:
    print(free)
else:
    print(dang)
