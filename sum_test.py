import unittest

import sumhello


class TestSum(unittest.TestCase):

	def test_sum(self):
		self.assertEqual(sumhello.mysum([1, 2, 3]), 6, "Should be 6")

	def test_sum_tuple(self):
		self.assertEqual(sumhello.mysum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
	unittest.main()