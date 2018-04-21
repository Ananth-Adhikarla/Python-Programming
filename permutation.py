"""
Please submit the following in a file named `permutation.py`.

1. For a list of integers L of length n, write a function `isPermutation(L)` returns True if L is a re-ordering of the integers from 1 up to n and False otherwise. For example, if `L = [1,2,4,3,5]`, `isPermutation(L)` should return True, because since n = 5, L is just a reordering of the numbers from 1 to 5. `L = [1,3,2,5,4]` would also return True. If `L = [1,2,3,-5,8,0]`, `isPermutation(L)` should return False. Similarly, `isPermutation([1,1,2,3,4,5])` should return False. You may not use any sorting functionality.

"""

"""
Condition 1 : Element should be less than length(N)
condition 2 : Element should not have negative value
condition 3 : Element should not have duplicates

"""


def isPermutation(L):

	seen = set()

	flag = False

	for element in L:
		seen.add(element)

	# Length of Original 
	
	length = len(L)
	
	# Length of Set

	length2 = len(seen)

	print("Original Values",L," Original length", len(L) )
	print("")
	print("Set Values",seen , " Set Length ", len(seen))
	print("")

	if( length != length2 ):
		return flag

	for element in L:
		if(element < 0):
			return flag

		elif(element > length):
			return flag
		
	

	flag = True

	print("The list ",L," Is a permutation list \n")

	return flag








#-----------------------------------------------------------------------------------------------------------------------------

a = [1,2,3,4,5]
b = [1,3,2,4,5]
c = [1,2,3,-5,8,0]
d = [1,1,2,3,4,5]

print("Test Case 1 \n\n")
print(isPermutation( list(a) ))

print("Test Case 2 \n\n")
print(isPermutation( list(b) ))

print("Test Case 3 \n\n")
print(isPermutation( list(c) ))

print("Test Case 4 \n\n")
print(isPermutation( list(d) ))
