sa = {}
for i in range(int(input())):
    if not sa.get(k := input(), 0):
        sa[k] = 1
    else:
        sa[k] += 1
count = 0
for i in sa:
    if sa[i] > 1:
        count += sa[i]
print(count)
