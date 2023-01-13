a = input()
b = int(a[2]) + int(a[1])
c = int(a[1]) + int(a[0])
print(max(b, c), min(b, c), sep='')