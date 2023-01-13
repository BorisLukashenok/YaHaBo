a = int(input())
b = int(input())
c = int(input())
b += c % 60
a += c // 60 + b // 60
a %= 24
b %= 60
print(f"{str(a).zfill(2)}:{str(b).zfill(2)}")
