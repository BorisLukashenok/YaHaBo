def prost(number: int):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False


a = int(input())
s = 0
for i in range(a):
    if prost(int(input())):
        s += 1
print(s)
