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
        self.znak = 1
        if self.num < 0:
            self.znak = -self.znak
            self.num = abs(self.num)
        if self.den < 0:
            self.znak = -self.znak
            self.den = abs(self.den)

    def numerator(self, *arg):
        match len(arg):
            case 0:
                return self.num
            case 1:
                self.num = arg[0]
                if self.num < 0:
                    self.znak = -self.znak
                    self.num = abs(self.num)
                self.__decrease()

    def denominator(self, *arg):
        match len(arg):
            case 0:
                return self.den
            case 1:
                self.den = arg[0]
                if self.den < 0:
                    self.znak = -self.znak
                    self.den = abs(self.den)
                self.__decrease()

    def __str__(self) -> str:
        return f'{"-" if self.znak < 0 else ""}{self.num}/{self.den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__str__()}')"

    def __neg__(self):
        return Fraction(-(self.num * self.znak), self.den)

    def __add__(self, other):
        return Fraction(self.znak * self.num * other.den +
                        other.znak * other.num * self.den,
                        self.den * other.den)

    def __iadd__(self, other):
        self.num = self.znak * self.num * other.den + other.znak * other.num * self.den
        self.den = self.den * other.den
        self.__minus()
        self.__decrease()
        return self

    def __sub__(self, other):
        return Fraction(self.znak * self.num * other.den -
                        other.znak * other.num * self.den,
                        self.den * other.den)

    def __isub__(self, other):
        self.num = self.znak * self.num * other.den - other.znak * other.num * self.den
        self.den = self.den * other.den
        self.__minus()
        self.__decrease()
        return self

    def __mul__(self, other):
        return Fraction(self.znak * self.num * other.znak * other.num,
                        self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.znak * self.num * other.znak * other.den,
                        self.den * other.num)

    def __imul__(self, other):
        self.num *= other.num
        self.den *= other.den
        self.znak *= other.znak
        self.__decrease()
        return self

    def __itruediv__(self, other):
        self.num = self.num * other.den
        self.den = self.den * other.num
        self.znak *= other.znak
        self.__decrease()
        return self

    def reverse(self):
        return Fraction(self.den * self.znak, self.num)

    def __float__(self):
        return self.num / self.den * self.znak

    def __eq__(self, other):
        return float(self) == float(other)

    def __lt__(self, other):
        return float(self) < float(other)
        
    def __le__(self, other):
        return float(self) <= float(other)

a = Fraction(1, 3)
b = Fraction(1, 2)
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
a = Fraction(1, 3)
b = Fraction(6, 2).reverse()
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)