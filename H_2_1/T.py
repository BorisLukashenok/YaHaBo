n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
a = 1
while a * k1 + (n - a) * k2 != n * m:
    a += 1
print(a, n - a)
