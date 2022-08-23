#!/usr/bin/python3
def uppercase(str):
	for i in str:
		value = ord(i)
		if value not in range(65, 91):
			print(chr(value - 32), end="")
		else:
			print(chr(value), end="")
