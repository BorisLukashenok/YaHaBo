sps = []
while (s := input()) != '':
    if not s.endswith('@@@'):
        sps.append(s.lstrip('##'))
for i in sps:
    print(i)
