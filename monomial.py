class Monomial:
	def __init__(self, coefficient, exponent):
		self.coefficient = coefficient
		self.exponent = exponent

	def __call__(self):
		return self

	def __str__(self):
		return str(self.coefficient) + "x^" + str(self.exponent)

print(Monomial(5,3))
