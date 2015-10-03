import unittest

import sys
sys.path.insert(0, '../')
import numerals

class NumeralsTest (unittest.TestCase):
	def test_we_have_dict(self):
		self.assertEqual(numerals.units[0], "efes")

	def test_we_convert_units_to_text(self):
		self.assertEqual(numerals.number_to_txt(1), "ehad")

	def test_we_convert_ten_to_text(self):
		self.assertEqual(numerals.number_to_txt(10), "eser")

	def test_we_convert_tens_to_text(self):
		self.assertEqual(numerals.number_to_txt(11), "ehadesre")

	def test_we_connvert_twenties_to_text(self):
		self.assertEqual(numerals.number_to_txt(22), "esrim veshtaim")








def main():
    unittest.main()

if __name__ == '__main__':
	main()