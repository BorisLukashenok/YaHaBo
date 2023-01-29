from sys import stdin

strring = input().casefold()
fails = []
for line in stdin.read().replace('\n', ' ').casefold().split():
    with open(line, encoding="utf-8") as op:
        if strring in ' '.join(op.read().replace("&nbsp;", " ").replace('\n', ' ').casefold().split()):
            fails.append(line)
if len(fails):
    print(*fails, sep='\n')
else:
    print('404. Not Found')
 