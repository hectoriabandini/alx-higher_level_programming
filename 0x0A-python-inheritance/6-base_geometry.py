#!/usr/bin/python3
"""Defines base geometry class BaseGeometry."""


class BaseGeometry:
    """Rep base geometry."""

    def area(self):
        """if not implemented."""
        raise Exception("area() is not implemented")
