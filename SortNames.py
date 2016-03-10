#!/usr/bin/python3

from PythonStructures.BinaryTree import TreeNode

__author__ = "Sam Schmalzried"

__names__ = TreeNode(None)

def AddName(name, tree):
	root = tree
	if root == None:
		root = TreeNode(name)
	elif root.getData() == None:
		root.setData(name)
	else:
		if name < root.getData():
			if root.getLeft() == None:
				root.setLeft(None)
			AddName(name, root.getLeft())
		elif name > root.getData():
			if root.getRight() == None:
				root.setRight(None)
			AddName(name, root.getRight())
		else:
			print("Name already sorted.")

def GetName():
	name = input("Enter a name: ")
	return name

def PrintNames(tree):
	root = tree
	if root == None:
		return
	else:
		PrintNames(root.getLeft())
		print(root.getData())
		PrintNames(root.getRight())

i = 0
while i < 10:
	name = GetName()
	AddName(name, __names__)
	i += 1

PrintNames(__names__)
