import os
import random


class NoSolutionFound(OSError):
	pass


class N2:

	@classmethod
	def digitsum(this, n):
		digits = [int(n) for n in list(str(n))]
		return sum(digits)
		

	@classmethod
	def solve(this, n):
		x = 1
		y = x + n

		while True:
			if (this.digitsum(x) == this.digitsum(y)):
				break
			x += 1
			y += 1

			if (n % 9 != 0):
				raise NoSolutionFound()

		return (x, y)


if __name__ == '__main__':
	file = open("N2.in")
	file.seek(4, os.SEEK_SET)

	for line in file:
		n = int(line)

		try:
			xy = N2.solve(n)
		except NoSolutionFound:
			print("NONE")
		else:
			print("%d %d" % (xy[0], xy[1]))