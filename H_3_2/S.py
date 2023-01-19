sa = set()
sb = set()
for i in range(int(input())):
    a = input()
    sc = set(a[a.find(":") + 2:].split(', '))
    sb |= sa & sc
    sa ^= sc
    sa -= sb
print('\n'.join(sorted(sa)))
