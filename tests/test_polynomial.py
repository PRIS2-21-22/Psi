import unittest
from src.polynomial import Monomial, Polynomial

class TestPolynomial(unittest.TestCase):
	def test_add(self):
		a = Polynomial([Monomial(-3,3), Monomial(2,2), Monomial(2,0)])
		b = Polynomial([Monomial(-2,2), Monomial(1,1), Monomial(1,0)])
		result = Polynomial([Monomial(-3,3), Monomial(1,1), Monomial(3,0)])

		self.assertEqual(a + b, result)
		self.assertEqual(a + b, b + a)

	def test_sub(self):
		a = Polynomial([Monomial(-3,3), Monomial(2,2), Monomial(2,0)])
		b = Polynomial([Monomial(-2,2), Monomial(1,1), Monomial(1,0)])
		result = Polynomial([Monomial(-3,3), Monomial(4,2), Monomial(-1,1), Monomial(1,0)])

		self.assertEqual(a - b, result)
		self.assertEqual(b - a, ~result)

	def test_mul(self):
		a = Polynomial([Monomial(2,2), Monomial(1,0)])
		b = Polynomial([Monomial(-2,2), Monomial(1,1), Monomial(1,0)])
		result = Polynomial([Monomial(-4,4), Monomial(2,3), Monomial(1,1), Monomial(1,0)])

		self.assertEqual(a * b, result)
		self.assertEqual(a * b, b * a)

#	def test_div(self):
#		a = Polynomial([Monomial(5,4), Monomial(8,3), Monomial(13,1), Monomial(4,0)])
#		b = Polynomial([Monomial(1,1), Monomial(3,0)])
#		result = Polynomial([Monomial(5,3), Monomial(-7,2), Monomial(21,1), Monomial(-50,0)])
#
#		self.assertEqual(a / b, result)

	def test_simplify(self):
		a = Polynomial([Monomial(-3,3), Monomial(4,2), Monomial(-2,2), Monomial(2,1), Monomial(1,1), Monomial(-1,1), Monomial(2,0)])
		result = Polynomial([Monomial(-3,3), Monomial(2,2), Monomial(2,1), Monomial(2,0)])

		self.assertEqual(a, result)


if __name__ == '__main__':
    unittest.main()
