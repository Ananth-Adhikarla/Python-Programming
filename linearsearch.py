"""
Linear Search
"""


def linear_search(dataset):
	
	key = int(input("Enter the key to search in list	"))
	flag = False
	
	for i in range(len(dataset)):
		if(dataset[i] == key):
			flag = True
			print("Found the key : ", key , " in the index " , i)
			break;
		
	if(flag == False):
		print("The key you are searching for is not found " )

	"""
	for i,j in enumerate(dataset):
		if(key == j):
			return i
	"""





l = [1,2,3,4,5,6,7,8,9,10,12]

print("Original List : ", l )

linear_search(l)

arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122]
print("\n")
print("Original List : ", arr )
linear_search(arr)
