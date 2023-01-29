summ = 0
with open('sample01_10c35fbe0c.num', 'rb') as f:
    while (dec := f.read(2)):
        summ += int.from_bytes(dec)
    print(summ)
