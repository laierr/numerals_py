import unittest

import sys
sys.path.insert(0, '../')
import numerals

class Selftest (unittest.TestCase):
	def test(self):
		assert True
	
	def test_import(self):
		assert numerals.selftest()


def main():
    unittest.main()


if __name__ == '__main__':
	main()