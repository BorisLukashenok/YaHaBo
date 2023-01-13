x = 0
y = 0
while (dire := input()) != "СТОП":
    if dire == "СЕВЕР":
        x += int(input())
    if dire == "ВОСТОК":
        y += int(input())
    if dire == "ЮГ":
        x -= int(input())
    if dire == "ЗАПАД":
        y -= int(input())
print(x, y, sep='\n')
