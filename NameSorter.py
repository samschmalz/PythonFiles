#!/usr/bin/python3

from PythonStructures.BinaryTree import TreeNode

__author__ = "Sam Schmalzried"

def ReadFile(filename):
	inFile = open(filename)
	first = inFile.readline()
	names = TreeNode(first)
	for line in inFile:
		AddName(names, line)
	inFile.close()
	return names

def AddName(tree, name):
	if tree == None:
		tree = TreeNode(name)
	elif tree.data > name:
		AddName(tree.leftChild, name)
	elif tree.data < name:
		AddName(tree.rightChild, name)
	else:
		print("Name already stored")

def PrintNames(tree, filename):
	if tree == None:
		return
	PrintNames(tree.leftChild, filename)
	outFile = open(filename, 'a')
	outFile.write(tree.data + "\n")
	outFile.close()
	PrintNames(tree.rightChild, filename)

inFile = input("Enter a file to read: ")
nameTree = ReadFile(inFile)
outFile = input("Enter a file to write: ")
PrintNames(nameTree, outFile)
