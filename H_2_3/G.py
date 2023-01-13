def nod(a, b):
    while b:
        a, b = b, a % b
    return a


a = int(input())
b = int(input())
print(int((a * b) / nod(a, b)))
