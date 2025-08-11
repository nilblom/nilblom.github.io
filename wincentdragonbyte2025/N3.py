import os
import random


class NoSolutionFound(OSError):
	pass


class N3:

	@classmethod
	def digitsum(this, n):
		digits = [int(n) for n in list(str(n))]
		return sum(digits)
		

	@classmethod
	def solve(this, n):
		if (n % 9 != 0):
			raise NoSolutionFound()

		x = 1
		y = x + n
	
		while True:
			if (this.digitsum(x) == this.digitsum(y)):
				break
			
			y = random.randint(0, 99999999999999999999999999999999999999999999999999)
			x = y - n

		return (x, y)


if __name__ == '__main__':
	file = open("N3.in")
	file.seek(4, os.SEEK_SET)

	for line in file:
		n = int(line)

		try:
			xy = N3.solve(n)
		except NoSolutionFound:
			print("NONE")
		else:
			print("%d %d" % (xy[0], xy[1]))