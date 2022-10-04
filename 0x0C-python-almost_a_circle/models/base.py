#!/usr/bin/python3
"""
"""


import json

class Base():
	"""
	"""

	__nb_objects = 0

	def __init__(self, id=None):
		if id != None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		"""
		"""
		if list_dictionaries is None or list_dictionaries == []:
			return "[]"
		return json.dumps(list_dictionaries)
	
	@classmethod
	def save_to_file(cls, list_objs):
		"""
		"""
		with open(cls.__name__ + ".json", "w") as file:
			if list_objs is None:
				file.write("[]")
			else:
				list_dictionaries = []
				for obj in list_objs:
					list_dictionaries.append(obj.to_dictionary())
				file.write(Base.to_json_string(list_dictionaries))

	@staticmethod
	def from_json_string(json_string):
		"""
		"""
		if json_string is None or json_string == "[]":
			return []
		return json.loads(json_string)