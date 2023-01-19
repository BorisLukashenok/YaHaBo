s = {input() for i in range(int(input()))}
for i in range(int(input())):
    for j in range(int(input())):
        s -= set([input()])
if len(s):
    for i in sorted(s):
        print(i)
else:
    print('Готовить нечего')
