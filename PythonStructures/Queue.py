#!/usr/bin/python3

__author__ = "Sam Schmalzried"

class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, x):
		self.items.append(x)

	def dequeue(self):
		return self.items.pop(0)

	def count(self):
		return len(self.items)
