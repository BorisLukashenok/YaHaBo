from sys import stdin
sps = []
for s in stdin:
    if not s.startswith('#'):
        if (temp := s.find('#')) == -1:
            temp = len(s)
        sps.append(s[:temp])
for i in sps:
    print(i.rstrip('\n'))
