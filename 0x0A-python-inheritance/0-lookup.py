#!/usr/bin/python3
def lookup(obj):
# Get the list of object attributes and methods
	obj_attributes = dir(obj)
	return obj_attributes
