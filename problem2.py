# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. 
# Solve it without using division and in O(n) time.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# brainstorming 
# trivially solvable with division since result[i] is the input.prod() / input[i]
# bruteforce would be O(n^2)


example1 = [1,2,3,4,5]

from functools import reduce
from operator import mul

# Method using reduce
# Unsure of compexity, but I have a feeling it is O(n^2) 
def arraymult(arr):
	return [reduce(mul, arr[:i] +arr[i+1:], 1) for i in xrange(len(arr))]


print arraymult(example1)