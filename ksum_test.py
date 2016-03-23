import pytest
import itertools
import sys

# Assumptions:
# 1. the file is small enough to be loaded all at once, in reasonable time
# 2. argument types are correct


# Complexity of bruteforce = number of combinations
# There are n! / (k! * (n-k)!) permutations,
# so complexity is O(n! / (k! * (n-k)!))
# which is itself O(n ^ min(k, n-k))
def ksum_bruteforce(k, s, numbers):
	for t in itertools.combinations(numbers, k):
		if sum(t) == s:
			return t
	raise ValueError("No solution")


@pytest.mark.parametrize("k, s, numbers, expected", [
	(3, 51, [7, 3, 6, 10, 43, 54, 2], (6, 43, 2)), # sample provided
	(1, 5, [3, 4, 5, 6], (5,)), # using only 1 number
	(1, 4, [4], (4,)), # only 1 number provided
	(3, 15, [4, 5, 6], (4, 5, 6)), # k == len(numbers)
])
def test_ksum_valid(k, s, numbers, expected):
	assert ksum_bruteforce(k, s, numbers) == expected

@pytest.mark.parametrize("k, s, numbers", [
	(3, 300, [7, 3, 6, 10, 43, 54, 2]), # no solution
	(1, 1, [3, 4, 5, 6]), # no solution
	(1, 3, [4]), # no solution
	(3, 2, [2, 3]), # k > len(numbers)
	(10, 0, [10]), # k == 0
	(10, -2, [10]), # k < 0
])
def test_ksum_invalid(k, s, numbers):
	with pytest.raises(ValueError):
		ksum_bruteforce(k, s, numbers)




if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("need a filename")
	else:
		with open(sys.argv[1]) as f:
			lines = [int(l[:-1]) for l in f]
			res = ksum_bruteforce(lines[0], lines[1], lines[2:])
			for i in res:
				print(i)