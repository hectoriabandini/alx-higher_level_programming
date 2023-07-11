#!/usr/bin/python3

def inherits_from(obj, a_class):
	"""Get the set of classes that obj is an instance of """
	obj_classes = set(type(obj).__mro__)

	""" Check if a_class is present in the set of classes"""
	return any(a_class in cls.__mro__ for cls in obj_classes)
