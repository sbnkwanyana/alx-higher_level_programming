#!/usr/bin/python3
"""
"""

from rectangle import Rectangle


class Square(Rectangle):
	"""
	"""

	def __init__(self, size, x=0, y=0, id=None):
		"""
		"""
		super().__init__(width=size, height=size,x=x, y=y, id=id)

	@property
	def size(self):
		"""
		"""
		return self.__width

	@size.setter
	def size(self, value):
		"""
		"""
		self.width = value
		self.height = value

	def __str__(self):
		"""
		"""
		return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

	def to_dictionary(self):
		"""
		"""
		return { "id":self.id, "size":self.__width, "x":self.__x, "y":self.__y }