#!usr/bin/python

__author__ = "Sam Schmalzried"

def BubbleSort(array):
	n = len(array)
	while n > 0:
		m = 1
		while m < n:
			if array[m] < array[m-1]:
				temp = array[m]
				array[m] = array[m-1]
				array[m-1] = temp
			m += 1
		n -= 1
	return array
