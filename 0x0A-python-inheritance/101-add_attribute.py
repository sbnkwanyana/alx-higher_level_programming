#!/usr/bin/python3
def add_attribute(self, attribute, value):
    """Add attribute if it's possible."""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")