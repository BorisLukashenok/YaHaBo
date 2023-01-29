from json import dump, load
from sys import stdin

with open(input(), 'r+', encoding="utf-8") as js:
    old_dict = load(js)
    js.seek(0)
    for line in stdin.readlines():
        key, val = line.rstrip('\n').split(' == ')
        old_dict[key] = val
    dump(old_dict, js, ensure_ascii=False, indent="\t")
