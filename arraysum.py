# Given an array and an input k, calculate if any two elements sum to k 
# Solution is O(n^2) with some trimming of impossible solutions 

#input: 
# @param array of positive integers 
# @param k the sum we are searching for 
def checkforsum(arr, k):
	for i in arr:
		if i > k:
			continue
		else:
			for j in arr:
				if i + j == k:
					return i,j
		return False

print(checkforsum([5,10,1,2,3,4], 9))