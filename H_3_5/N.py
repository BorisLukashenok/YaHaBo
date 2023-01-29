from json import dump, load
file = input()
with open(file, encoding="utf-8") as js, open(input(), encoding="utf-8") as add:
    old_dict = load(js)
    add_dict = load(add)
new_dict = {}
new_add_dict = {}

for d in old_dict:
    new_dict[d.pop('name')] = d
for d in add_dict:
    new_add_dict[d.pop('name')] = d
for k, v in new_dict.items():
    if k in new_add_dict:
        for kk in new_add_dict[k].keys():
            if kk in new_dict[k]:
                if new_add_dict[k][kk] > new_dict[k][kk]:
                    new_dict[k][kk] = new_add_dict[k][kk]
            else:
                new_dict[k][kk] = new_add_dict[k][kk]
with open(file, 'w', encoding="utf-8") as js:
    dump(new_dict, js, ensure_ascii=False, indent="\t")
