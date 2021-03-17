class Monomial:
	def __init__(self, coefficient, exponent):
		self.coefficient = coefficient
		self.exponent = exponent #TODO: comprobar que no sea negativo

	def __str__(self):
		return str(self.coefficient) + "x^" + str(self.exponent)


class Polynomial:
	def __init__(self, monomials):
		self.monomials = monomials.copy()#.sort()
		#self.monomials = monomials

	#def __add__(self, other):
		#return Polynomial()

	#def __sub__(self, other):
		#return Polynomial()

	#def __mul__(self, other):
		#return Polynomial()

	def __str__(self):
		return str(self.monomials)

test = Polynomial([Monomial(2, 4), Monomial(6, 3)])
#test = Polynomial(5)
print(test)
