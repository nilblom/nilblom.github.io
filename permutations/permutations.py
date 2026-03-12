def swap(arr, i, j):
    copy = arr[i]
    arr[i] = arr[j]
    arr[j] = copy


def find_successor(arr, i):
    j = 1
    lim = max(arr) * 2
    while True:
        for k in range(0, len(arr)):
            if arr[k] == arr[i]+j:
                return k
        j += 1
        if j > lim:
            break
    return i


def find_max(d):
    max = 0
    for i in range(0, len(d)):
        if d[i] > d[max]:
            max = i
    return max


def sort_from(arr, start):
    i = len(arr)-1
    while i >= start:
        m = max(arr[start:i+1])
        swap(arr, i, start+arr[start:i+1].index(m))
        i -= 1

arr = [1, 2, 3, 4, 11, 10, 9, 8, 7, 6, 5]
sort_from(arr, 5)
assert arr == [1, 2, 3, 4, 11, 5, 6, 7, 8, 9, 10]


def permutations(data):
    start = 0
    end = len(data)-1
    indices = [x for x in range(0, end+1)]
    yield from _permutations(data, indices, start, end)


def _permutations(data, indices, start, end):
    for _ in range(0, end+1-start):
        if (end-start == 1):
            yield [data[i] for i in indices]

        if (end+1-start) > 1:
            yield from _permutations(data, indices, start+1, end)

        s = find_successor(indices[start:], 0)
        swap(indices, start+s, start)
        sort_from(indices, start+1)
            

if __name__ == "__main__":
    for x in permutations(["a", "b", "c", "d"]):
        print(x)
