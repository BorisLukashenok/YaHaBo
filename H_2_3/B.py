count = 0
while (txt := input()) != "Приехали!":
    if "зайка" in txt:
        count += 1
print(count)