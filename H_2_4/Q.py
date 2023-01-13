a = int(input())
count = 0
for i in range(a):
    if (a := input()) == a[::-1]:
        count += 1
print(count)
