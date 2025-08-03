from math import gcd

class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        # Reduce numerator and denominator by their greatest common divisor
        g = gcd(numer, denom)
        numer //= g
        denom //= g
        # Ensure the denominator is positive
        if denom < 0:
            numer = -numer
            denom = -denom
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numer == other.numer and self.denom == other.denom
        return NotImplemented

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        n = self.numer * other.denom + other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        n = self.numer * other.denom - other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        # Integer exponent
        if isinstance(power, int):
            if power == 0:
                return Rational(1, 1)
            if power > 0:
                return Rational(self.numer ** power, self.denom ** power)
            # Negative integer exponent
            if self.numer == 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power.")
            p = -power
            return Rational(self.denom ** p, self.numer ** p)
        # Real (floating-point) exponent -> returns a float
        return (self.numer / self.denom) ** power

    def __rpow__(self, base):
        # Real number raised to a rational exponent
        return base ** (self.numer / self.denom)
