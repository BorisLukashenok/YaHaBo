znak = '+-*/'
stek = []
for i in input().split():
    if i in znak:
        a1 = stek.pop()
        a2 = stek.pop()
        match i:
            case '+':
                stek.append(a2 + a1)
            case '-':
                stek.append(a2 - a1)
            case '*':
                stek.append(a2 * a1)
            case '/':
                stek.append(a2 / a1)
    else:
        stek.append(int(i))
print(*stek)
