#!/usr/bin/python3
""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle

class Square(Rectangle):
	""" A square from the rectangle class"""
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)
	def __str__(self):
		return ("[Square] ({}) {}/{} - {}".format(self.id,\
		 self.x, self.y, self.width, self.height))


	@property
	def size(self):
		"""get the width property"""
		return self.width
	@size.setter
	def size(self, value):
		self.width = value
		self.height=value

	def update(self, *args, **kwargs):
		"""Adding keywords arg and possitional args
		update the rectangle with key and positional args
		args:width(int)
		height(int)
		x(int)
		y (int)
		"""
		num_args = len(args)
		if num_args >= 1:
			self.id = args[0]
		if num_args >= 2:
			self.size = args[1]
		if num_args >= 3:
			self.x = args[2]
		if num_args >= 4:
			self.y = args[3]

		if args:
			kwargs = {}

		for key, value in kwargs.items():
			if key == 'id':
				self.id = value
			elif key == 'size':
				self.size = value
			elif key == 'x':
				self.x = value
			elif key == 'y':
				self.y = value
