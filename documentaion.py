
def binary_search(l, i):
	# l: a sorted array of integer values
	# i: is the number we wnat to find
	# return: the index of i if i exists, otherwise return -1
	assert(l == sorted(l))
	if len(l) == 0:
		return -1
	else:
		mid = len(l)/2
		if l[mid]>i:
			return binary_search (l[:mid], i)
		elif l[mid]==i:
			return mid 
		else:
			return mid + 1 + binary_search(l[mid+1:], i)


