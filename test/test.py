import unittest

import sys
sys.path.insert(0, '../')
import numerals

class NumeralsTest (unittest.TestCase):
	def test_we_have_dict(self):
		self.assertEqual(numerals.units[0], "efes")

	def test_we_convert_units_to_text(self):
		self.assertEqual(numerals.number_to_txt(1), "ehad")

	def test_we_convert_tens_precise_to_text(self):
		self.assertEqual(numerals.number_to_txt(10), "eser")

	def test_we_convert_tens_to_text(self):
		self.assertEqual(numerals.number_to_txt(11), "ehadesre")

	def test_we_convert_twenties_to_text(self):
		self.assertEqual(numerals.number_to_txt(22), "esrim veshtaim")

	def test_we_convert_hundreds_precise_to_text(self):
		self.assertEqual(numerals.number_to_txt(100), "mea")

	def test_we_convert_hundreds_wo_tens_to_text(self):
		self.assertEqual(numerals.number_to_txt(101), "mea veehad")

	def test_we_convert_hundreds_and_ten_to_text(self):
		self.assertEqual(numerals.number_to_txt(111), "mea veehadesre")

	def test_we_convert_hundreds_to_text(self):
		self.assertEqual(numerals.number_to_txt(121), "mea esrim veehad")


def main():
    unittest.main()

if __name__ == '__main__':
	main()