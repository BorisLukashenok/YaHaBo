class Fraction:
    def __init__(self, *args) -> None:
        match len(args):
            case 1:
                self.num, self.den = (map(int, args[0].split('/')))

            case 2:
                self.num = args[0]
                self.den = args[1]
        self.znak = 1
        self.__minus()
        self.__decrease()

    def __gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def __decrease(self):
        delit = self.__gcd(self.num, self.den)
        self.num //= delit
        self.den //= delit

    def __minus(self):
        if self.den < 0:
            self.znak *= -1
            self.den = abs(self.den)
        if self.num < 0:
            self.znak *= -1
            self.num = abs(self.num)

    def numerator(self, *arg):
        match len(arg):
            case 0:
                return self.num
            case 1:
                self.num = arg[0]
                self.__minus()
                self.__decrease()

    def denominator(self, *arg):
        match len(arg):
            case 0:
                return self.den
            case 1:
                self.den = arg[0]
                self.__minus()
                self.__decrease()

    def __str__(self) -> str:
        return f'{"-" if self.znak < 0 else ""}{self.num}/{self.den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__str__()}')"

    def __neg__(self):
        return Fraction(-(self.num * self.znak), self.den)


a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))
a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
