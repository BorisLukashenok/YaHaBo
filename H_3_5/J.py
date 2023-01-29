with open(input(), encoding="UTF-8") as op:
    print(*op.readlines()[-int(input()):], sep="")