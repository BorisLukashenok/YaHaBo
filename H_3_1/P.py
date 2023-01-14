long = int(input())
s = []
for i in range(int(input())):
    s.append(input())
out = '\n'.join(s)
t = out[:long - 3].count('\n')
t = out[:long - 3 + t].count('\n')
print(out[:long - 3 + t] + "...")