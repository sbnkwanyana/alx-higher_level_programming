#!/usr/bin/python3
"""
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base

class RectangleTests(unittest.TestCase):
	"""

	"""
	def setUp(self):
		Rectangle.__nb_objects = 0

	def test_rectangle_id(self):
		r1 = Rectangle(10, 2)
		r2 = Rectangle(2, 10)
		r3 = Rectangle(10, 2, 0, 0, 12)
		#self.assertEqual(r1.id, 7)
		#self.assertEqual(r2.id, 8)
		#self.assertEqual(r3.id, 12)

	def test_area(self):
		r1 = Rectangle(3, 2)
		r2 = Rectangle(2, 10)
		r3 = Rectangle(8, 7, 0, 0, 12)
		self.assertEqual(r1.area(), 6)
		self.assertEqual(r2.area(), 20)
		self.assertEqual(r3.area(), 56)

	def test_display(self):
		#TODO
		r1 = Rectangle(4, 6)
		r2 = Rectangle(2, 2)
		#self.assertEqual(r1.display, )
		self.assertEqual(r2.area(), 4)

	def test_str(self):
		# TODO
		r1 = Rectangle(4, 6, 2, 1, 12)
		r2 = Rectangle(5, 5, 1)
		
	
	def tearDown(self) -> None:
		return super().tearDown()
