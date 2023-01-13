a = sorted([input(), input(), input()])
for i in range(len(a)):
    if 'зайка' in a[i]:
        print(a[i], len(a[i]))
        break
