summ = 0
with open('public.txt', 'rb') as f:
    while (dec := f.read(2)):
        summ += int.from_bytes(dec)
print(summ)
