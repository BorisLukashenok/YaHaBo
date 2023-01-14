leng = int(input())
sps = []
for i in range(int(input())):
    if len(s := input()) > leng:
        sps.append(s[:leng - 3] + "...")
    else:
        sps.append(s)
for i in sps:
    print(i)
