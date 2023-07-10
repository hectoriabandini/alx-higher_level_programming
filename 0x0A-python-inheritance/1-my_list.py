#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
	"""Implementation of sorted printing for the built-in list class."""

	def print_sorted(self):
		"""Printing a list in sorted ascending order."""
		print(sorted(self))
