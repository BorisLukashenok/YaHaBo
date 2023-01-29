with open(input(), encoding="UTF-8") as op:
    list_num =list(map(int, op.read().replace('\n', ' ').split()))
count_plus = 0
for i in list_num:
    if i > 0:
        count_plus += 1


print(len(list_num), count_plus, min(list_num),
      max(list_num), sum(list_num), round(sum(list_num) / len(list_num), 2), sep='\n')
