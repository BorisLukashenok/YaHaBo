sa = set()
while (s := input()) != '':
    for t in range(len(p := s.split())):
        if p[t] == "зайка":
            sa |= set(p[t-1: t])
            sa |= set(p[t+1: t+2])
print('\n'.join(i for i in sa))