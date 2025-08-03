import math

class ComplexNumber:
    """
    A class to represent and operate on complex numbers.

    Attributes:
        real (float): The real part of the complex number.
        imaginary (float): The imaginary part of the complex number.
    """
    def __init__(self, real, imaginary):
        """
        Initialize a new ComplexNumber instance.

        Args:
            real (float): Real part.
            imaginary (float): Imaginary part.
        """
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        """
        Check equality between two complex numbers.

        Args:
            other (ComplexNumber): Another complex number to compare.

        Returns:
            bool: True if both real and imaginary parts are equal.
        """
        if isinstance(other, ComplexNumber):
            return (self.real == other.real) and (self.imaginary == other.imaginary)
        return NotImplemented

    def __add__(self, other):
        """
        Add a complex or real number to this complex number.

        Supports ComplexNumber + ComplexNumber and ComplexNumber + real.
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary
            )
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)
        return NotImplemented

    __radd__ = __add__  # Support real + ComplexNumber

    def __sub__(self, other):
        """
        Subtract a complex or real number from this complex number.
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real - other.real,
                self.imaginary - other.imaginary
            )
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imaginary)
        return NotImplemented

    def __rsub__(self, other):
        """
        Subtract this complex number from a real number: real - complex.
        """
        if isinstance(other, (int, float)):
            return ComplexNumber(other, 0).__sub__(self)
        return NotImplemented

    def __mul__(self, other):
        """
        Multiply this complex number by another complex or real number.
        """
        if isinstance(other, ComplexNumber):
            # (a + bi)(c + di) = (ac - bd) + (bc + ad)i
            real = self.real * other.real - self.imaginary * other.imaginary
            imag = self.imaginary * other.real + self.real * other.imaginary
            return ComplexNumber(real, imag)
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imaginary * other)
        return NotImplemented

    __rmul__ = __mul__  # Support real * ComplexNumber

    def __truediv__(self, other):
        """
        Divide this complex number by another complex or real number.
        """
        if isinstance(other, ComplexNumber):
            # (a + bi)/(c + di) = [(ac + bd) + (bc - ad)i] / (c^2 + d^2)
            denom = other.real**2 + other.imaginary**2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denom
            imag = (self.imaginary * other.real - self.real * other.imaginary) / denom
            return ComplexNumber(real, imag)
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imaginary / other)
        return NotImplemented

    def __rtruediv__(self, other):
        """
        Divide a real number by this complex number: real / complex.
        """
        if isinstance(other, (int, float)):
            return ComplexNumber(other, 0).__truediv__(self)
        return NotImplemented

    def __abs__(self):
        """
        Return the absolute value (modulus) of the complex number.

        |z| = sqrt(a^2 + b^2)
        """
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        """
        Return the complex conjugate of the number.
        """
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """
        Compute the complex exponential using Euler's formula:
        e^(a + bi) = e^a (cos b + i sin b).

        Returns:
            ComplexNumber: The exponential of this complex number.
        """
        magnitude = math.exp(self.real)
        return ComplexNumber(
            magnitude * math.cos(self.imaginary),
            magnitude * math.sin(self.imaginary)
        )

    def __repr__(self):
        """
        Return the code-like representation of ComplexNumber.
        """
        return f"ComplexNumber({self.real}, {self.imaginary})"
