#!/usr/bin/python

import sys, re
from function import *
from calcul import *

def main():
	if (len(sys.argv) == 2):
		argv = sys.argv[1].split('=')
		equationLst = fillArray(argv[0])
		solutionLst = fillArray(argv[1])
		positiveArr = factoEqua(equationLst)
		negativeArr = negArray(factoEqua(solutionLst))

		reduced = reducedArray(positiveArr, negativeArr)
		degree = printReducedForm(reduced)
		if (degree > 2):
			print 'The polynomial degree is stricly greater than 2, I can\'t solve.'
			return 0
		handleDegree(degree, reduced)
	elif (len(sys.argv) > 2):
		print 'Too few arguments'
	else:
		print 'Put one argument'

if __name__ == '__main__':
	main()
