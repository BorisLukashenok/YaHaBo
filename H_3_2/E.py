a = int(input())
b = int(input())
sa = dict()
for i in range(a + b):
    if sa.get(s := input(), 1):
        sa.setdefault(s)
    else:
        del sa[s]
print('Таких нет' if not len(sa) else len(sa))
