
print(*filter(lambda x: not sum(map(int, str(x))) % 2, (32, 64, 128, 256, 512)))


# lambda x: not x if sum(map(int, str(x))) % 2 else x