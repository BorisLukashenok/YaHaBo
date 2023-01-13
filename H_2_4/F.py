def nod(a, b):
    while b:
        a, b = b, a % b
    return a


a = int(input())
n = int(input())
for i in range(a - 1):
    n = nod(n, int(input()))
print(n)
