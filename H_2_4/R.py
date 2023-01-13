a = int(input())
count = 0
t = 0
s = ''
sps = []
for i in range(1, a + 1):
    if t > 0 and i < a:
        s += str(i) + ' '
        t -= 1
    elif t == 0 or i == a:
        s += str(i)
        sps.append(s)
        count += 1
        t = count
        s = ''
t = len(sps) * 2 + len(str(a)) - 1
for i in range(len(sps)):
    print(f'{sps[i]:^{t}}')
