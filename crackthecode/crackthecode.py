from collections import deque
import random
import copy
from itertools import combinations, permutations, product

"""
Crack the code is a game where a secret code must be solved
by using tips that partially reveal the code.

Each tip has the form x y numbers where x is the number of
numbers in the tip that also exist in the code. y is the
number of numbers in the tip that are correctly placed.

The numbers in the tip add up to a set of numbers. The code
is made up of a set of these numbers.

The crackthecode function takes a list of tips, from which
it infers what the code is.

Codes have the form [a, b, c] where no number is repeated.
"""

def negative_hypotheses(a):
	results = []
	q = deque(a)
	for i in range(3):
		q.rotate(1)
		results.append(list(q))
	return results

a = [5, 0, 6]
n = negative_hypotheses(a)
assert n == [[6, 5, 0], [0, 6, 5], [5, 0, 6]]

def mirror_numbers(a):
	numbers = []
	b = copy.copy(a)
	for i in range(3):
		if a[i] != "_":
			numbers.append(a[i])
	for i in range(3):
		if a[i] != "_":
			b[i] = numbers.pop(-1)
		else:
			b[i] = "_"
	if b == a:
		return None
	return b

test_numbers = [1, 2, "_"]
mirror_numbers(test_numbers) == [2, 1, "_"]


def infer(x, y, a):
	if x < y:
		raise Exception("x must be equal to or greater than y")

	if x == 0:
		H = [ [[1, ["_", "_", "_"]]] ]
		n = negative_hypotheses(a)
		for h in n:
			H[0].append([0, h])
		return H

	P = list(permutations(a))

	results = []
	seen_positive_hypotheses = []
	for permutation in P:

		b = list(permutation)
		C = list(combinations(b, x))

		for combination in C:
			combination = list(combination)
			c = copy.copy(b)
			correctly_placed = 0
			exclude = [0, ["_", "_", "_"]]

			for number in range(3):
				if c[number] in combination and c[number] == a[number]:
					correctly_placed += 1

				if c[number] not in combination:
					exclude[1][number] = c[number]
					c[number] = "_"

			if correctly_placed != y:
				continue

			if c in seen_positive_hypotheses:
				continue

			seen_positive_hypotheses.append(c)

			c = [1, c]

			if mirror_numbers(exclude[1]):
				results.append((c, exclude, [0, mirror_numbers(exclude[1])]))
			else:
				results.append((c, exclude))

	return results


def solution_fits(solution):
	for i in range(3):
		a = None

		def find_digit():
			for h in solution:
				for x in h:
					if x[0] == 1 and x[1][i] != "_":
						return x[1][i]

		a = find_digit()
		for h in solution:
			for x in h:
				if x[0] == 1:
					if x[1][i] != a and x[1][i] != "_":
						return False
				elif x[0] == 0:
					if x[1][i] == a and x[1][i] != "_":
						return False
	return True


def flatten(L):
	L = list(L)
	L[0] = list(L[0])
	L[0].extend(L[1:])
	L = L[0]
	return L

L = ((1, 2), 3)
L = flatten(L)
assert L == [1, 2, 3]


def combine_cheap(H, callback):
	i = 1
	C = H[0]
	while i < len(H):
		C = list(product(C, H[i]))
		k = 0
		while i > 1 and k < len(C):
			C[k] = flatten(C[k])

			# solution_fits() is inserted here as a
			# "callback", so that combine_cheap() can
			# have a clean test-case.
			if not callback(C[k]):
				C.pop(k)
			else:
				k += 1
		i += 1
	return C


a = [[1, 2, 3, 4], [1], [1, 2], [1, 2, 3]]
r = combine_cheap(a, lambda x: True)
#print(r)
assert r == [
	[1, 1, 1, 1],
	[1, 1, 1, 2],
	[1, 1, 1, 3],
	[1, 1, 2, 1],
	[1, 1, 2, 2],
	[1, 1, 2, 3],
	[2, 1, 1, 1],
	[2, 1, 1, 2],
	[2, 1, 1, 3],
	[2, 1, 2, 1],
	[2, 1, 2, 2],
	[2, 1, 2, 3],
	[3, 1, 1, 1],
	[3, 1, 1, 2],
	[3, 1, 1, 3],
	[3, 1, 2, 1],
	[3, 1, 2, 2],
	[3, 1, 2, 3],
	[4, 1, 1, 1],
	[4, 1, 1, 2],
	[4, 1, 1, 3],
	[4, 1, 2, 1],
	[4, 1, 2, 2],
	[4, 1, 2, 3]
]

# Remains for speed comparisons.
# def combine(H):
# 	results = []
# 	combinations = product(*H)
# 	for c in combinations:
# 		if solution_fits(c):
# 			results.append(c)
# 	return results


def simple_form(solution):
	simple = [-1, -1, -1]
	for hyp in solution:
		hyp = hyp[0]
		if hyp[0] == 0:
			continue
		for i in range(3):
			if hyp[1][i] != "_":
				simple[i] = hyp[1][i]       
	return simple


def solution_is_complete(simple_form):
	if -1 in simple_form:
		return False
	return True


def crackthecode(tips):
	hypotheses = []
	for tip in tips:
		hypotheses.append(list(infer(tip[0], tip[1], tip[2])))

	solutions = combine_cheap(hypotheses, solution_fits)
	unique_solutions = []
	
	for s in solutions:
		t = simple_form(s)
		if not solution_is_complete(t):
			continue
		if t not in unique_solutions:
			unique_solutions.append(t)

	return unique_solutions


def generate_tips(code):

	def infer_x(code, a):
		x = 0
		for number in a:
			if number in code:
				x += 1
		return x

	def infer_y(code, a):
		y = 0
		for i in range(3):
			if code[i] == a[i]:
				y += 1
		return y

	def tips_contains_code(tips, code):
		digits = []
		for x, y, numbers in tips:
			digits.extend(numbers)
		for d in code:
			if d not in digits:
				return False
		return True

	tips = []

	while True:
		tips = []
		while len(tips) < 4:
			pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

			numbers = [pool.pop(random.randint(0, len(pool)-1)),
				pool.pop(random.randint(0, len(pool)-1)),
				pool.pop(random.randint(0, len(pool)-1))]
			
			x = infer_x(code, numbers)
			y = infer_y(code, numbers)

			tips.append((x, y, numbers))

		if tips_contains_code(tips, code):
			break

	return tips



if __name__ == '__main__':

	h = infer(1, 1, [4, 7, 8])
	if h == [
		([1, [4, '_', '_']], [0, ['_', 7, 8]], [0, ['_', 8, 7]]),
		([1, ['_', 7, '_']], [0, [4, '_', 8]], [0, [8, '_', 4]]),
		([1, ['_', '_', 8]], [0, [4, 7, '_']], [0, [7, 4, '_']])
	]:
		print("test 1 1 pass")

	h = infer(1, 0, [9, 1, 5])
	if h == [
		([1, ['_', 5, '_']], [0, [9, '_', 1]], [0, [1, '_', 9]]),
		([1, ['_', '_', 1]], [0, [9, 5, '_']], [0, [5, 9, '_']]),
		([1, [1, '_', '_']], [0, ['_', 9, 5]], [0, ['_', 5, 9]]),
		([1, ['_', 9, '_']], [0, [1, '_', 5]], [0, [5, '_', 1]]),
		([1, ['_', '_', 9]], [0, [1, 5, '_']], [0, [5, 1, '_']]),
		([1, [5, '_', '_']], [0, ['_', 9, 1]], [0, ['_', 1, 9]])
	]:
		print("test 1 0 pass")

	h = infer(2, 2, [8, 6, 3])
	if h == [
		([1, [8, 6, '_']], [0, ['_', '_', 3]]),
		([1, [8, '_', 3]], [0, ['_', 6, '_']]),
		([1, ['_', 6, 3]], [0, [8, '_', '_']])
	]:
		print("test 2 2 pass")

	h = infer(2, 0, [8, 6, 3])
	if h == [
		([1, ['_', 3, 6]], [0, [8, '_', '_']]),
		([1, [6, 8, '_']], [0, ['_', '_', 3]]),
		([1, [6, 3, '_']], [0, ['_', '_', 8]]),
		([1, [6, '_', 8]], [0, ['_', 3, '_']]),
		([1, ['_', 3, 8]], [0, [6, '_', '_']]),
		([1, [3, 8, '_']], [0, ['_', '_', 6]]),
		([1, [3, '_', 6]], [0, ['_', 8, '_']]),
		([1, ['_', 8, 6]], [0, [3, '_', '_']]),
		([1, [3, '_', 8]], [0, ['_', 6, '_']])
	]:
		print("test 2 0 pass")

	h = infer(2, 1, [1, 3, 5])
	if h == [
		([1, [1, 5, '_']], [0, ['_', '_', 3]]),
		([1, [1, '_', 3]], [0, ['_', 5, '_']]),
		([1, [3, '_', 5]], [0, ['_', 1, '_']]),
		([1, ['_', 1, 5]], [0, [3, '_', '_']]),
		([1, [5, 3, '_']], [0, ['_', '_', 1]]),
		([1, ['_', 3, 1]], [0, [5, '_', '_']])
	]:
		print("test 2 1 pass")

	h = infer(0, 0, [1, 2, 3])
	if h == [
		[[1, ['_', '_', '_']],
			[0, (1, 2, 3)],
			[0, (1, 3, 2)],
			[0, (2, 1, 3)],
			[0, (2, 3, 1)],
			[0, (3, 1, 2)],
			[0, (3, 2, 1)]]
	]:
		print("test 0 0 pass")
	# An interesting extension to the program is to support
	# numbers that are not in the tips, but can occur in the
	# secret code.

	# The program cannot also handle cases where a digit occurs
	# twice in the tip.
	#
	# h = infer(1, 1, [1, 2, 2])
	# print(h)
	# if h == [
	#       ([1, [1, '_', '_']], [0, ['_', 2, 2]]),
	#       ([1, ['_', '_', 2]], [0, [2, 1, '_']], [0, [1, 2, '_']]),
	#       ([1, ['_', 2, '_']], [0, [1, '_', 1]])
	# ]:
	#   print("test 1 1 (multiple occurence of digits) pass")

	# Solution: 3, 8, 2
	print("_________")
	print("Code: 382")
	tips = [(1, 1, [3, 0, 4]), (2, 1, [2, 8, 1]), (0, 0, [7, 1, 5]), (1, 1, [6, 9, 2])]
	for code in crackthecode(tips):
		print("Solution:", code)

	# Solution: 9, 6, 8
	print("_________")
	print("Code: 968")
	tips = [(1, 0, [6, 1, 4]), (2, 0, [0, 9, 6]), (1, 0, [5, 9, 3]), (0, 0, [4, 5, 0]), (1, 1, [4, 7, 8])]
	for code in crackthecode(tips):
		print("Solution:", code)

	# Solution: 1, 5, 8
	print("_________")
	print("Code: 158")
	tips = [(0, 0, [3, 4, 2]), (0, 0, [2, 7, 3]), (2, 1, [1, 6, 5]), (2, 1, [8, 5, 3]), (2, 0, [8, 6, 5])]
	for code in crackthecode(tips):
		print("Solution:", code)

	# Solution: 9, 8, 4
	print("_________")
	print("Code: 984")
	tips = [(1, 0, [2, 4, 5]), (1, 1, [9, 1, 0]), (2, 0, [8, 3, 9]), (0, 0, [1, 2, 6]), (1, 1, [6, 8, 1])]
	for code in crackthecode(tips):
		print("Solution:", code)

	# Solutions: [1, 2, 3], [2, 4, 9], [3, 9, 3], [5, 2, 3]
	print("_________")
	print("Code: 123")
	tips = [
		(1, 0, [3, 8, 4]),
		(1, 0, [9, 1, 5]),
		(0, 0, [8, 7, 8]),
		(2, 1, [3, 2, 9])
	]
	for code in crackthecode(tips):
		print("Solution:", code)

	print("_________")
	print("Code: 348")
	tips = [(2, 1, [3, 1, 4]), (0, 0, [5, 6, 0]), (1, 0, [2, 1, 4]), (2, 1, [3, 8, 7])]
	for code in crackthecode(tips):
		print("Solution:", code)

	print("_________")
	print("Code (generated tips): ", [1, 6, 3])
	tips = generate_tips([1, 6, 3])
	for t in tips:
		print("Tip: ", t)
	for code in crackthecode(tips):
		print("Found code: ", code)

	print("_________")
	print("Code: 163")
	tips = [
		(1, 1, [1, 7, 9]),
		(1, 1, [9, 8, 3]),
		(2, 2, [8, 6, 3]),
		(1, 1, [1, 7, 8])
	]
	for code in crackthecode(tips):
		print("Solution:", code)
