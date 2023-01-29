with open(input(), encoding="UTF-8") as op:
    list_one = set(op.read().replace('\n', ' ').split())
with open(input(), encoding="UTF-8") as op:
    list_two = set(op.read().replace('\n', ' ').split())

with open(input(), 'w', encoding="UTF-8") as op:
    list_two = op.write('\n'.join(sorted(list_one ^ list_two)))
