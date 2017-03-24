import unittest
import rpn
import time
import termcolor
import sys

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_exponentiation(self):
		result = rpn.calculate('2 3 ^')
		self.assertEqual(8, result)
	finalOutput = "All tests have passed. Congratulations!"
	for x in range(0, len(finalOutput)):
		if(x % 2 == 0):
			print(termcolor.colored(finalOutput[x], "red")),
		else:
			print(termcolor.colored(finalOutput[x], "green")),
		sys.stdout.flush()
		time.sleep(1)
		#This is a comment	
