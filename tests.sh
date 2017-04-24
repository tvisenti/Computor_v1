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
	printf "Equa: 5 + 4 * X + X^2= X^2\n"
	python computor.py  "5 + 4 * X + X^2= X^2"
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

{
	printf "Equa: -2 * X^0 + 43 * X^1 - 9.3 * X^2 + 12 * X^0 - 45 * X^1 = 0\n"
	python computor.py  "-2 * X^0 + 43 * X^1 - 9.3 * X^2 + 12 * X^0 - 45 * X^1 = 0"
	echo '-----'
}

{
	printf "Equa: 4 * X^2 - 9 * X^2 = 123\n"
	python computor.py  "4 * X^2 - 9 * X^2 = 123"
	echo '-----'
}

{
	printf "Equa: 4 * X^2 - 9 * X^1 = 123\n"
	python computor.py  "4 * X^2 - 9 * X^1 = 123"
	echo '-----'
}

{
	printf "Equa: 42 * X^0 + 1 = 42 * X^0 + 1124153133464636457774563468776454657735346\n"
	python computor.py  "42 * X^0 + 1 = 42 * X^0 + 1124153133464636457774563468776454657735346"
	echo '-----'
}

{
	printf "Equa: 42 * X^0 + 4 * X^1 - 16 * X^2 = 21 + 46 * X^1 + 5 * X^2\n"
	python computor.py  "42 * X^0 + 4 * X^1 - 16 * X^2 = 21 + 46 * X^1 + 5 * X^2"
	echo '-----'
}

{
	printf "Equa: 42 * X^0 + 4 * X^1 - 16 * X^2 + 42 * X^42 = -21 + 46 * X^1 + 5 * X^2 + 42 * X^42\n"
	python computor.py  "42 * X^0 + 4 * X^1 - 16 * X^2 + 42 * X^42 = 21 + 46 * X^1 + 5 * X^2 + 42 * X^42"
	echo '-----'
}

{
	printf "Equa: 42 * X^0 + 4 * X^1 - 16 * X^2 + 41 * X^42 = -21 + 46 * X^1 + 5 * X^2 + 42 * X^42\n"
	python computor.py  "42 * X^0 + 4 * X^1 - 16 * X^2 + 41 * X^42 = 21 + 46 * X^1 + 5 * X^2 + 42 * X^42"
	echo '-----'
}

{
	printf "Equa: 42 + 4 * X - X^2 = -21 + 46 * X\n"
	python computor.py  "42 + 4 * X - X^2 = -21 + 46 * X"
	echo '-----'
}
