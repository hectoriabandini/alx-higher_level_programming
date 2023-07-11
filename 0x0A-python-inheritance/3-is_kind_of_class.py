#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ Check if the object is an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    
    """Check if the object is an instance of a class that inherited from the specified class"""
    for cls in obj.__class__.mro():
        if cls is a_class:
            return True
    
    return False
