a = int(input())
name_vin = ''
sums = 0
for i in range(a):
    name = input()
    if (s := sum(map(int, input()))) >= sums:
        name_vin = name
        sums = s
print(name_vin)
