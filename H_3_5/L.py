with open(input(), encoding="utf-8") as num, open(input(), 'w', encoding="utf-8") as even:
    with open(input(), 'w', encoding="utf-8") as odd, open(input(), 'w', encoding="utf-8") as eq:
        for line in num.readlines():
            for num in line.split():
                count = 0
                for i in num:
                    if int(i) % 2:
                        count += 1
                match count:
                    case _ if count < len(num) - count:
                        print(num, end=' ', file=even)
                    case _ if count > len(num) - count:
                        print(num, end=' ', file=odd)
                    case _ if count == len(num) - count:
                        print(num, end=' ', file=eq)
            print(file=even)
            print(file=odd)
            print(file=eq)
