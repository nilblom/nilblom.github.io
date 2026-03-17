def combinations(data, n):
    indices = [x for x in range(0, len(data))]
    combination = []
    yield from _combinations(data, combination, indices, n, 0)

def _combinations(data, combination, indices, n, i):
    if n == 0:
        yield tuple([data[i] for i in combination])
        return

    j = i
    while j < len(indices):
        combination.append(indices.pop(j))
        yield from _combinations(data, combination, indices, n-1, j)
        indices.insert(j, combination.pop(-1))
        j += 1

for c in combinations(["A", "B", "C", "D"], 3): print(c)
