
print([{"digits": len(bin(i).replace("0b", "")), "units": bin(i).replace("0b", "").count(
    "1"), "zeros": bin(i).replace("0b", "").count("0")} for i in (list(map(int, input().split(" "))))])
