with open(input(), encoding="UTF-8") as op:
    stroka = '\n'.join([i for i in map(lambda x: ' '.join(
        x.split()), op.read().replace('\t', '').split('\n')) if i])
with open(input(), 'w', encoding="UTF-8") as op:
    op.write(stroka)
