#!/usr/bin/python3

__author__ = "Sam Schmalzried"

class Stack:
	def __init__(self):
		self.items = []

	def Push(self, data):
		self.items.append(data)

	def Peek(self):
		num = len(self.items) - 1
		return self.items[num]

	def Pop(self):
		return self.items.pop()

	def Count(self):
		return len(self.items)
