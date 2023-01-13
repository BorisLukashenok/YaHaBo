n = int(input())
print("А Б В")
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if n - i - j - k == 0:
                print(i, j, k)
