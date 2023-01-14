flag = True
for i in range(int(input())):
    if not input().startswith(('а', 'б', 'в')):
        flag = False
print('YES' if flag else 'NO')
