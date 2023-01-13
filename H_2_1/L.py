a = int(input())
b = int(input())
i = 10
ans = 0
while a or b:
    ans += ((a % 10 + b % 10) % 10) * i
    a //= 10
    b //= 10
    i *= 10
print(ans // 10)
