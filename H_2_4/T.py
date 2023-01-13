a = int(input())
max_sum = syst = 0
for i in range(2, 11):
    b = ''
    n = a
    while n > 0:
        b = str(n % i) + b
        n = n // i
    if (s := sum(map(int, b))) > max_sum:
        max_sum = s
        syst = i
print(syst)
