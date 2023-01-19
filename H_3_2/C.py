s = set()
for i in range(int(input())):
    s |= set(input().split())
for i in s:
    print(i)