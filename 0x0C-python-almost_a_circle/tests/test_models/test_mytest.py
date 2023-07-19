#!/usr/bin/python3
import unittest
from base import Base

class MyTestCase(unittest.TestCase):
	def test_args_id(self):
		b1 = base()
		
		self.assertEqual(b1.id, 1)

	def test_argid(self):
		pass

if __name__ ==" __main__":
	unittest.main()
