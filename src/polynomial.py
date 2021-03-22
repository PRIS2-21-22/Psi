class Monomial:
	def __init__(self, coefficient, exponent):
		if exponent < 0:
			raise ValueError("Exponent cannot be negative.", exponent)

		self.coefficient = coefficient
		self.exponent = exponent

	def __add__(self, other):
		if self.exponent != other.exponent:
			raise ValueError("Exponents must be equal.", self.exponent, other.exponent)

		return Monomial(self.coefficient + other.coefficient, self.exponent)

	def __sub__(self, other):
		return self + ~other

	def __invert__(self):
		return Monomial(-self.coefficient, self.exponent)

	def __lt__(self, other):
		return self.exponent < other.exponent if self.exponent != other.exponent else self.coefficient < other.coefficient

	def __le__(self, other):
		return (self < other) or (self == other)

	def __eq__(self, other):
		return (self.coefficient == other.coefficient) and (self.exponent == other.exponent)

	def __ne__(self, other):
		return not(self == other)

	def __gt__(self, other):
		return not(self <= other)

	def __ge__(self, other):
		return not(self < other)

	def __str__(self):
		if self.coefficient == 0:
			return ""
		elif self.coefficient > 0:
			coeff = " +" if self.coefficient == 1 and self.exponent != 0 else " +" + str(self.coefficient)
		else:
			coeff = " -" if self.coefficient == -1 and self.exponent != 0 else " -" + str(-self.coefficient)

		if self.exponent > 1:
			x = "x^" + str(self.exponent)
		elif self.exponent == 1:
			x = "x"
		else:
			x = ""

		return coeff + x


class Polynomial:
	def __init__(self, monomials = None):
		if monomials is None:
			self.monomials = []
		else:
			self.monomials = monomials.copy()
			self.fillGaps()

	def __add__(self, other):
		result = Polynomial()
		longList  = self.monomials if (len(self.monomials) > len(other.monomials)) else other.monomials
		shortList = self.monomials if (len(self.monomials) < len(other.monomials)) else other.monomials

		for i in range(0, len(shortList)):
			result.monomials.append(shortList[i] + longList[i])

		result.monomials.extend(longList[len(shortList):])
		result.fillGaps()
		return result

	def __sub__(self, other):
		return self + ~other

	#def __mul__(self, other):
		#return

	#def __truediv__(self, other):
		#return

	def __invert__(self):
		inverted = Polynomial()
		for i in self.monomials:
			inverted.monomials.append(~i)
		return inverted

	def __eq__(self, other):
		if len(self.monomials) != len(other.monomials):
			return False

		areEqual = True
		for i in range(0, len(self.monomials)):
			if self.monomials[i] != other.monomials[i]:
				areEqual = False
				break

		return areEqual

	def __ne__(self, other):
		return not(self == other)

	def __str__(self):
		if len(self.monomials) == 0:
			return ""

		string = "".join([str(i) for i in self.monomials]).strip()
		if string[0] == "+":
			string = " " + string[1:]

		return string

	def readFile(self, filepath):
		file = open(filepath, "r")
		for i in file.readlines():
			line = i[:i.find("#")]
			if line.strip() == "":
				continue

			splitted = line.split(",")
			coeff = int(splitted[0])
			exp   = int(splitted[1])

			if coeff == exp == 0:
				break

			self.monomials.append(Monomial(coeff, exp))

		file.close()
		self.fillGaps()
		return self

	def fillGaps(self):
		self.monomials.sort()
		length = len(self.monomials) - 1
		if self.monomials[length].exponent == length:  # Already filled
			return

		extension = []
		expected = 0
		for i in self.monomials:
			if i.exponent != expected:
				for j in range(expected, i.exponent):
					extension.append(Monomial(0, j))
			expected = i.exponent + 1

		self.monomials.extend(extension)
		self.monomials.sort()
