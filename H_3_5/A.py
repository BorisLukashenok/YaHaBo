from sys import stdin

print(sum([sum(map(int, i.split())) for i in stdin]))
