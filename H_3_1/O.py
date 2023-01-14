def nod(a, b):
    while b:
        a, b = b, a % b
    return a


s = input().split()
n = int(s[0])
for i in range(1, len(s)):
    n = nod(n, int(s[i]))
print(n)
