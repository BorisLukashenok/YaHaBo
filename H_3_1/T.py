def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


znak_bin = '+-*/'
znak_unar = '~!#'
znak_ter = '@'
stek = []
for i in input().split():
    if i in znak_bin:
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
                stek.append(a2 // a1)
    elif i in znak_unar:
        a1 = stek.pop()
        match i:
            case '~':
                stek.append(-a1)
            case '#':
                stek.extend([a1, a1])
            case '!':
                stek.append(fac(a1))
    elif i in znak_ter:
        a1 = stek.pop()
        a2 = stek.pop()
        a3 = stek.pop()
        stek.extend([a2, a1, a3])
    else:
        stek.append(int(i))
print(*stek)
