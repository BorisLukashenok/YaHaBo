class Fraction:
    def __init__(self, *args) -> None:
        match len(args):
            case 1:
                self.num, self.den = (map(int, args[0].split('/')))

            case 2:
                self.num = args[0]
                self.den = args[1]
        self.__decrease()

    def __gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def __decrease(self):
        delit = self.__gcd(self.num, self.den)
        self.num //= delit
        self.den //= delit

    def numerator(self, *arg):
        match len(arg):
            case 0:
                return self.num
            case 1:
                self.num = arg[0]
                self.__decrease()

    def denominator(self, *arg):
        match len(arg):
            case 0:
                return self.den
            case 1:
                self.den = arg[0]
                self.__decrease()

    def __str__(self) -> str:
        return f'{self.num}/{self.den}'

    def __repr__(self) -> str:
        return f'Fraction({self.num}, {self.den})'


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))
fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
