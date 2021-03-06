#!/usr/bin/env python3

import operator
#This is a comment....
OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	#'%': operator.mod,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
						
			stack.append(result)
	#print("This is a test!")
	return stack.pop()

def one_plus_one():
	numOnePointFive = 1.5
	numNegPointFive = -0.5
	numOne = numOnePointFive - numNegPointFive
	return numOne

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)

if __name__ == '__main__':
	main()
