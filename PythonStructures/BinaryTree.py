#!/usr/bin/python3

__author__ = "Sam Schmalzried"

class TreeNode:
	def __init__(self, initial=None):
		self.data = initial
		self.leftChild = None
		self.rightChild = None

	def getData(self):
		return self.data

	def setData(self, info):
		self.data = info

	def getLeft(self):
		return self.leftChild

	def getRight(self):
		return self.rightChild

	def setLeft(self, info):
		self.leftChild = TreeNode(info)

	def setRight(self, info):
		self.rightChild = TreeNode(info)
