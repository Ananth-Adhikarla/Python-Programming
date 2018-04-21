"""
Insert Sort
"""


def insertion_sort(nlist):
	
	for i in range(1,len(nlist)):
		temp = nlist[i]

		j = i
		
		while( j>0 and temp < nlist[j - 1]):
			nlist[j] = nlist[j-1]
			j -= 1
		
		nlist[j] = temp 
		
	return nlist


l = [1,3,5,7,4,2]

print("Original List : ",l)


print("After insert sort ", insertion_sort(l) )


assert insertion_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert insertion_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
assert insertion_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
