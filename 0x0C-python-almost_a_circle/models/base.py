#!/usr/bin/python3
import json

class Base:
	"""This class will be the base of all other classes in this project.
	private class attribute __nb_objects
	"""
	__nb_objects = 0
	
	def __init__(self, id=None):
	"""The goal of it is to manage id attribute in all your future classes"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
	"""json method converting list_dictionaries to json strings"""
		if list_dictionaries is None or len(list_dictionaries) == 0:
			return "[]"
		else:
			return json.dumps(list_dictionaries)
	@classmethod
	def save_to_file(cls, list_objs):
	""""The goal of it is to manage id attribute in all your future 
	classes and to avoid duplicating the same code (by extension, same bugs)
	"""
		if list_objs is None:
			list_objs = []
		filename = cls.__name__ + ".json"
		json_data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
		with open(filename, 'w') as file:
			file.write(json_data)
	@staticmethod
	def from_json_string(json_string):
	"""Converting json to a string"""
		if json_string is None or len(json_string) == 0:
			return "[]"
		else:
			return json.loads(json_string)
