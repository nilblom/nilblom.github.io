def cartesian_product(data, callback):
	max_lengths = [len(x)-1 for x in data]
	indices = [0 for x in data]
	_cartesian_product(indices, max_lengths, len(data)-1, callback)


def _cartesian_product(indices, max_lengths, i, callback):
	while indices[i] <= max_lengths[i]:
		for k in range(0, i):
			indices[k] = 0
		if i > 0:
			_cartesian_product(indices, max_lengths, i-1, callback)
		if i == 0:
			callback(indices)
		if indices[i] == max_lengths[i]:
			break
		indices[i] += 1


if __name__ == '__main__':
	data = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
	cartesian_product(data, lambda x: print([data[i][x[i]] for i in range(len(data))]))
