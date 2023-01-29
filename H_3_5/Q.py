with open("secret.txt", encoding='utf-8') as f:
    data = f.read()
for i in data:
    if ord(i) > 128:
        print(chr(int(bin(ord(i))[-8:], 2)), end='')
    else:
        print(i, end='')
