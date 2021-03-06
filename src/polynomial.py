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

	def __mul__(self, other):
		return Monomial(self.coefficient * other.coefficient, self.exponent + other.exponent)

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
			self.fill_gaps()

	def __add__(self, other):
		result = Polynomial()
		long_list  = self.monomials if (len(self.monomials) > len(other.monomials)) else other.monomials
		short_list = self.monomials if (len(self.monomials) < len(other.monomials)) else other.monomials

		for i in range(0, len(short_list)):
			result.monomials.append(short_list[i] + long_list[i])

		result.monomials.extend(long_list[len(short_list):])
		result.fill_gaps()
		return result

	def __sub__(self, other):
		return self + ~other

	def __mul__(self, other):
		result = []

		for i in self.monomials:
			for j in other.monomials:
				result.append(i * j)

		return Polynomial(result)

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

		are_equal = True
		for i in range(0, len(self.monomials)):
			if self.monomials[i] != other.monomials[i]:
				are_equal = False
				break

		return are_equal

	def __ne__(self, other):
		return not(self == other)

	def __str__(self):
		if len(self.monomials) == 0:
			return ""

		string = "".join([str(i) for i in self.monomials]).strip()
		if string[0] == "+":
			string = " " + string[1:]

		return string

	def read_file(self, filepath):
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
		self.fill_gaps()
		return self

	# Fills the gaps in the polynomial by adding monomials with coefficient zero.
	def fill_gaps(self):
		self.monomials.sort()
		self.simplify()
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

	def simplify(self):
		# Adds a dummy element at the end of the array. Not present in the result.
		self.monomials.append(Monomial(0,0))

		result = []
		current_list = []
		current_exp = self.monomials[0].exponent
		for i in self.monomials:
			if i.exponent != current_exp:
				sum = Monomial(0, current_exp)
				for j in current_list:
					sum = sum + j

				result.append(sum)
				current_exp = i.exponent
				current_list = []

			current_list.append(i)

		self.monomials = result.copy()
