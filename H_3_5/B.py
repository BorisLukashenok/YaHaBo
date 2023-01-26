from sys import stdin
s = []
for i in stdin:
    t = i.rstrip('\n').split()
    s.append(int(t[-1]) - int(t[-2]))
print(round(sum(s) / len(s)))
