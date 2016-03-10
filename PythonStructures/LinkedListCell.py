#!/usr/bin/python3

__author__ = "Sam Schmalzried"

class Cell:
	def __init__(self, initial):
		self.data = initial
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext
