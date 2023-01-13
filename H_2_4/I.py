a = int(input())
s = ''
for i in range(a):
    s += str(max(map(int, input())))
print(s)
