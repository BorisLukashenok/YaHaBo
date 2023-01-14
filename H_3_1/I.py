sps = []
while (s := input()) != '':
    if not s.startswith('#'):
        if (temp := s.find('#')) == -1:
            temp = len(s)
        sps.append(s[:temp])
for i in sps:
    print(i)