sa = {}
while (s := input()) != '':
    for i in s.split():
        if not sa.get(i, 0):
            sa[i] = 1
        else:           
            sa[i] += 1
for i in sa:
    print(i, sa[i])