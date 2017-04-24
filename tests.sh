#!/bin/sh

#
# This is a shell script in order to test your computor_v1 program.
#

{
	echo '-----------------------------------------------------------------'
	printf "\t\t\tTests from 42\n"
	echo '-----------------------------------------------------------------\n'
	printf "Equa: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\n"
	python computor.py  "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
	echo '-----'
}

{
	printf "Equa: 5 * X^0 + 4 * X^1 = 4 * X^0\n"
	python computor.py  "5 * X^0 + 4 * X^1 = 4 * X^0"
	echo '-----'
}

{
	printf "Equa: 8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0\n"
	python computor.py  "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
	printf "\n"
}

{
	echo '-----------------------------------------------------------------'
	printf "\t\t\tOthers tests\n"
	echo '-----------------------------------------------------------------\n'
	printf "Equa: 5*X^0=4*         X^0\n"
	python computor.py  "5*X^0 = 4           *         X^0"
	echo '-----'
}

{
	printf "Equa: 5 * X^2 = 5 * X^2\n"
	python computor.py  "5 * X^2 = 5 * X^2"
	echo '-----'
}
