flag = True
if (number := int(input())) > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("NO")
            flag = False
            break
    if flag:
        print('YES')
else:
    print('NO')
