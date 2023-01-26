from itertools import cycle

sps = cycle([input() for i in range(int(input()))])
for letter in range(int(input())):
    print(next(sps))
