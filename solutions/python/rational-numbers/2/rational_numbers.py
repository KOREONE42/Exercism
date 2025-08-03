from math import gcd

class Rational:
    """
    A class representing rational numbers in lowest terms (a/b).

    Supports addition, subtraction, multiplication, division,
    absolute value, and exponentiation (integer and real powers).
    """
    def __init__(self, numer, denom):
        """
        Initialize a Rational(numer, denom), reducing to lowest terms
        and ensuring a positive denominator.

        Raises ZeroDivisionError if denom is zero.
        """
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # Compute greatest common divisor and reduce
        common = gcd(numer, denom)
        numer //= common
        denom //= common

        # Normalize sign: keep denom positive
        if denom < 0:
            numer = -numer
            denom = -denom

        self.numer = numer  # Integer numerator
        self.denom = denom  # Integer denominator

    def __eq__(self, other):
        """
        Check equality of two Rationals by comparing reduced numerators and denominators.
        """
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        """
        Unambiguous string representation: 'numer/denom'.
        """
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        """
        Add two Rationals: a/b + c/d = (a*d + b*c) / (b*d).
        """
        if not isinstance(other, Rational):
            return NotImplemented
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        """
        Subtract two Rationals: a/b - c/d = (a*d - b*c) / (b*d).
        """
        if not isinstance(other, Rational):
            return NotImplemented
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        """
        Multiply two Rationals: (a/b) * (c/d) = (a*c) / (b*d).
        """
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        """
        Divide two Rationals: (a/b) / (c/d) = (a*d) / (b*c).

        Raises ZeroDivisionError if other is zero.
        """
        if not isinstance(other, Rational):
            return NotImplemented
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        """
        Absolute value: |a/b| = |a|/|b|, reduced.
        """
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        """
        Exponentiate Rational by an integer or real power.

        - Integer power: returns a new Rational.
            * r**0 = 1
            * r**n = (a^n)/(b^n) for n>0
            * r**-n = (b^n)/(a^n) for n>0
        - Real (float) power: returns a float (a/b)**power.
        """
        # Integer exponent case
        if isinstance(power, int):
            if power == 0:
                return Rational(1, 1)
            if power > 0:
                return Rational(self.numer ** power, self.denom ** power)
            # Negative integer exponent
            if self.numer == 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power.")
            exp = -power
            return Rational(self.denom ** exp, self.numer ** exp)

        # Fallback to real exponentiation, returning float
        return (self.numer / self.denom) ** power

    def __rpow__(self, base):
        """
        Raise a real base to this Rational exponent: base^(a/b) = (base**a)**(1/b).
        Returns a float.
        """
        return base ** (self.numer / self.denom)
