from sys import stdin
s = stdin.readlines()
z = s[-1].rstrip("\n").lower()
for i in s[: -1]:
    if z in i.lower():
        print(i.rstrip("\n"))
