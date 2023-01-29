def gcd(n, *num):
    def gccd(a, b):
        while b:
            a, b = b, a % b
        return a
    nod = n
    for i in num:
        nod = gccd(nod, i)
    return nod

print(gcd(3))
print(gcd(36, 48, 156, 100500))