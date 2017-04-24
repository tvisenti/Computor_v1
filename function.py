# Return offset for substring
def retOffset(string):
	plus = string.find('+')
	minus = string.find('-')
	if plus == 0 or minus == 0:
		plus = string[1:].find('+')
		minus = string[1:].find('-')
		if minus < 0 and plus < 0:
			return len(string)
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

def addIfExist(oldNb, newNb):
	if not oldNb:
		return float(newNb)
	return float(oldNb) + float(newNb)

# Factorize the array -> simplify reading
def factoEqua(array):
	index = 0
	newArray = [0] * 128
	while (index < len(array)):
		tmpStr = array[index].replace(' ', '')
		if (tmpStr.find('X') == -1):
			subIndex = len(tmpStr)
			spliting = tmpStr
			newArray[0] = addIfExist(newArray[0], spliting)
		else:
			if (tmpStr.find('X^') == -1):
				subIndex = tmpStr.find('X') + 1
				power = 1
				spliting = tmpStr.split('*')
			else:
				subIndex = tmpStr.find('X^') + 2
				power = int(tmpStr[subIndex:])
				spliting = tmpStr.split('*')
			if spliting[0].find('X') == -1:
				newArray[power] = addIfExist(newArray[power], spliting[0])
			else:
				if len(spliting) == 1:
					newArray[power] = addIfExist(newArray[power], 1)
				else:
					newArray[power] = addIfExist(newArray[power], spliting[1])
		index += 1
	return newArray

# Change values to opposite sign in array
def negArray(array):
	index = 0
	while (index < len(array)):
		array[index] *= -1
		index += 1
	return array

# Add second array in first array
def reducedArray(firstArr, secondArr):
	index = 0
	while (index < len(firstArr)):
		firstArr[index] += secondArr[index]
		index += 1
	return firstArr

# Print equation with the right form
def printReducedForm(array):
	index = 0
	degree = 0
	toPrint = 'Reduced form: '
	while (index < len(array)):
		if (array[index] != 0):
			tmp = str(array[index])
			if (tmp.find('-') == -1 and index > 0):
				toPrint += '+ '
			elif (tmp.find('-') != -1):
				toPrint += '- '
				tmp = tmp[1:]
			if (tmp.find('.0') != -1):
				degree = index
				toPrint += tmp[:tmp.find('.0')] + ' * X^' + str(index) + ' '
			else:
				degree = index
				toPrint += tmp + ' * X^' + str(index) + ' '
		index += 1
	toPrint += '= 0'
	if toPrint == 'Reduced form: = 0':
		toPrint = 'Reduced form: 0 = 0'
	print toPrint
	print 'Polynomial degree:', degree
	return degree
