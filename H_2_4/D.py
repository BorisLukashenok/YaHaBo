a = int(input())
s = 0
for i in range(a):
    s += sum(map(int, input()))
print(s)
