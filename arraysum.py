#Given an array of numbers, return whether any two sums to K.
#For example, given [10, 15, 3, 7] and K of 17, return true since 10 + 7 is 17.

# Solution is O(n^2) with some trimming of impossible solutions 
# Other solutions
# 	sort and then some sort of binary search within a range of valid answers to avoid the linear scan 
# 		This would give O(nlgn) 

#input: 
# @param array of positive integers 
# @param k the sum we are searching for 
def checkforsum(arr, k):
	for i in arr:
		if i > k:
			continue
		else:
			for j in arr:
				if i + j == k and i!=j:
					return i,j
		return False


def checkforsum_hash(arr,k):
	value_to_index = {}
	for i, num in enumerate(arr):
		value_to_index[num] = i
	for i, num in enumerate(arr):
		if (k-num) in value_to_index and i != value_to_index[k-num]:
			return True