sps = []
while (s := input()) != 'ФИНИШ':
    sps += s.lower().split()
s = ''.join(sorted(''.join(sps)))
ch_l = []
num_l = []
i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count = count + 1
        i = i + 1
    ch_l.append(s[i])
    num_l.append(count)
    i = i + 1
print(ch_l[num_l.index(max(num_l))])
