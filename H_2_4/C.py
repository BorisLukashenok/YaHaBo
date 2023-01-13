a = int(input())
count = 0
t = 0
for i in range(1, a + 1):
    if t > 0:
        print(i, end=' ')
        t -= 1
    else:
        print(i)
        count += 1
        t = count
