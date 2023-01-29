from json import dump

with open(input(), encoding="UTF-8") as op:
    list_num = list(map(int, op.read().replace('\n', ' ').split()))
count_plus = 0
for i in list_num:
    if i > 0:
        count_plus += 1


stat = {"count": len(list_num), "positive_count": count_plus, "min": min(list_num), "max": max(
    list_num), "sum": sum(list_num), "average": round(sum(list_num) / len(list_num), 2)}
with open(input(), "w", encoding="utf-8") as j:
    dump(stat, j, ensure_ascii=False, indent="\t")