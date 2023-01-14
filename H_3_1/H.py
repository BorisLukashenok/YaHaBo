s = []
for i in range(int(input())):
    s.append(input().find('зайка'))
for i in range(len(s)):
    print('Заек нет =(' if s[i] == -1 else s[i] + 1)
