#!/usr/bin/python

import sys, re

# Return offset for substring
def retOffset(string):
	plus = string.find('+')
	minus = string.find('-')
	if plus == 0 or minus == 0:
		if plus < 0 and minus == 0 or minus < 0 and plus == 0:
			return len(string)
		plus = string[1:].find('+')
		minus = string[1:].find('-')
		if plus < 0:
			return minus + 1
		elif minus < 0:
			return plus + 1
		return plus + 1 if plus < minus else minus + 1
	if plus <= 1:
		return minus
	elif minus <= 1:
		return plus
	return plus if plus < minus else minus

# Fill an array with right sequences
def fillArray(newExpression):
	offset = 1
	array = []
	while (offset > 0):
		offset = retOffset(newExpression)
		if offset < 0:
			break
		array.append(newExpression[:offset])
		newExpression = newExpression[offset:]
	if not array:
		array.append(newExpression)
	return array

# Return a float number
def	getFloat(string):
	spliting = string.replace(' ', '').split('*')
	index = 0
	while (index < len(spliting)):
		print "split: ", spliting[index]
		if (spliting[index].find('X') == -1):
			floating = float(spliting[index])
			print "Float: ", floating
			return floating
		index += 1

def addIfExist(oldNb, newNb):
	print oldNb
	print newNb
	if not oldNb:
		return float(newNb)
	return float(oldNb) + float(newNb)

# Factorize the array -> simplify reading
def factoEqua(array):
	index = 0
	newArray = [0] * 128
	while (index < len(array)):
		tmpStr = array[index].replace(' ', '')
		subIndex = tmpStr.find('X^') + 2
		power = int(tmpStr[subIndex:])
		spliting = tmpStr.split('*')
		print spliting
		if spliting[0].find('X') == -1:
			newArray[power] = addIfExist(newArray[power], spliting[0])
		else:
			newArray[power] = addIfExist(newArray[power], spliting[1])
		index += 1
	return newArray

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		argv = str(sys.argv[1])
		splitEqual = argv.split('=')
		newExpression = splitEqual[0]
		equationLst = fillArray(newExpression)
		newExpression = splitEqual[1]
		solutionLst = fillArray(newExpression)
		print "equationLst: ", equationLst
		print "solutionLst: ", solutionLst
		index = 0
		integer = []
		test = factoEqua(equationLst)
		print test
		# while (index < len(equationLst)):
		# 	integer.append(getFloat(equationLst[index]))
		# 	index += 1
		#
		# print integer

	elif (len(sys.argv) > 2):
		print 'Too few arguments'
	else:
		print 'Put one argument'

# def getOneEquation(delimiters, string):
#     regexPattern = '|'.join(map(re.escape, delimiters))
#     return re.split(regexPattern, string)
