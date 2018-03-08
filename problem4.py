# Problem 4 
# March 8, 2018

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def find_lowest_positive_int(arr):
	count, mysum = thesum(arr)
	expectedsum = ((count ) * (count + 1)) / 2
	if mysum - expectedsum == 0:
		return count + 1
	else:
		return mysum - expectedsum

def thesum(alist):
	s = 0
	c = 0
	for x in alist:
		if x>0:
			s = s+x
			c = c + 1
	return c,s

example1 = [3,4,-1,1]
print find_lowest_positive_int(example1)

example2 = [1,2,0]
print find_lowest_positive_int(example2)