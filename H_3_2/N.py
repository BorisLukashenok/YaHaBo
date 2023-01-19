r = {}
s = {input() for i in range(int(input()))}
for i in range(int(input())):
    b = input()
    r[b] = set()
    for j in range(int(input())):
        r[b].add(input())
flag = True
for i in sorted(r):
    if r[i] <= s:
        print(i)
        flag = False
if flag:
    print('Готовить нечего')
