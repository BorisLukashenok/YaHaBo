s = []
for i in range(int(input())):
    s.append(input())
zap = input().lower()
for i in s:
    if zap in i.lower():
        print(i)
