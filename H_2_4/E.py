a = int(input())
s = 0
for i in range(a):
    flag = True
    while (ans := input()) != 'ВСЁ':
        if flag and 'зайка' in ans:
            s += 1
            flag = False
print(s)
