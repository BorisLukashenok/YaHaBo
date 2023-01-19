long = int(input())
out = '\n'.join([input() for i in range(int(input()))])
t = out[:long - 3].count('\n')
t = out[:long - 3 + t].count('\n')