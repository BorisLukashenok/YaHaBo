import math

with open(input(), 'rb') as f:
    lenght = len(f.read())
pwr = math.floor(math.log(lenght, 1024))
suff = ["Б", "КБ", "МБ", "ГБ"]
print(f"{math.ceil(lenght / 1024 ** pwr)}{suff[pwr]}")
