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

    # def __call__(self, *args):
    #     pass
    
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


a = Fraction(-1, 3)
print(a)
a.numerator(-1)
print(a)
a.numerator(-a.numerator())
print(a)
b = Fraction(-2, 3)
c = a + b

print(a, b, c, a is c, b is c)
a = Fraction(1, 8)+ Fraction(1,8)
c = b = Fraction(3, 8)
b -= a 
print(a, b, c, b is c)
