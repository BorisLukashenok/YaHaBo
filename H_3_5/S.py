shift = int(input())
code = ''
with open('public.txt') as f:
    stroka = f.read()
for ch in stroka:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        ch = chr((ord(ch) - start + shift) % 26 + start)
    code += ch
with open('private.txt', 'w') as f:
    f.write(code)
