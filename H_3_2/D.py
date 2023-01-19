a = int(input())
b = int(input())
sa = set()
sb = set()
for i in range(a):
    sa.add(input())
for i in range(b):
    sb.add(input())
sa &= sb
print('Таких нет' if not len(sa) else len(sa))
