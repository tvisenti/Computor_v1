def handleDegree(degree, equa):
	if degree < 2:
		if degree == 0:
			r = equa[0]
		if degree == 1:
			r = (equa[0] / equa[1]) * -1
		print 'The solution is:\n', removeFloatingZero(r)
	else:
		r = solverSecondDegree(equa)


def solverSecondDegree(equa):
	delta = calculDelta(equa[2], equa[1], equa[0])
	if (delta < 0):
		print 'Discriminant is strictly negative, the two solutions are:'
		unrealNb = delta * -1
		print calculComplexPositif(unrealNb, equa[2], equa[1])
		print calculComplexNegatif(unrealNb, equa[2], equa[1])
	elif (delta == 0):
		print 'Discriminant is equal 0, the only solutions is:'
		print calculZero(equa[2], equa[1])
	else:
		print 'Discriminant is strictly positive, the two solutions are:'
		sqrt = my_sqrt(delta)
		print ("%.6f" % calculSupNegatif(sqrt, equa[2], equa[1]))
		print ("%.6f" % calculSupPositif(sqrt, equa[2], equa[1]))

def removeFloatingZero(nb):
	nb = str(nb)
	if (nb.find('.0') != -1):
		nb = nb[:nb.find('.0')]
	return nb

def calculDelta(a, b, c):
	return ((b * b) - (4 * a * c))

def calculComplexNegatif(unrealNb, a, b):
	a *= 2
	b = (b * -1) / a
	unrealNb = (my_sqrt(unrealNb))

	a = removeFloatingZero(a)
	b = removeFloatingZero(b)
	unrealNb = removeFloatingZero(unrealNb)
	if b == '0' or b == '-0':
		toPrint = '(i * ' + unrealNb + ') / ' + a
	else:
		toPrint = b + ' - (i * ' + unrealNb + ' / ' + a + ')'
	return toPrint

def calculComplexPositif(unrealNb, a, b):
	a *= 2
	b = (b * -1) / a
	unrealNb = (my_sqrt(unrealNb))

	a = removeFloatingZero(a)
	b = removeFloatingZero(b)
	unrealNb = removeFloatingZero(unrealNb)
	if b == '0' or b == '-0':
		toPrint = '(i * ' + unrealNb + ') / ' + a
	else:
		toPrint = b + ' + (i * ' + unrealNb + ' / ' + a + ')'
	return toPrint

def calculZero(a, b):
	return (b / (2 * a)) * -1

def calculSupNegatif(sqrt, a, b):
	return (((b * -1) - sqrt) / (2 * a))

def calculSupPositif(sqrt, a, b):
	return (((b * -1) + sqrt) / (2 * a))

def my_sqrt(number):
	error = 0.0001
	s = number

	while (error < (s - number / s)):
		s = ((s + number / s) / 2)

	return s
