from sys import stdin
s = sorted(set(stdin.read().replace('\n', ' ').split()))
for i in s:
    if i.lower() == i[:: -1].lower():
        print(i)
