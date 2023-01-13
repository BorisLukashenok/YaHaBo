def nod(a, b):
    while b:
        a, b = b, a % b
    return a


print(nod(int(input()), int(input())))
