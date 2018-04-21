"""
Binary Search
"""

#import wordlist.txt

def binary_search(dataset):
	
	key = int(input("Enter the key to search in list	"))
	#key = 3
	flag = False
	
	l = len(dataset)
	ll = l / 2	
	
	for i in range(len(dataset)):	
		if( dataset[int(ll)] == key):
			print("Found key : ", key , " in index " , int(ll) )
			flag = True
			break

		for j in range(0,int(ll)):
			if( key == dataset[j] ):
				print("Found key : ", key , " in index : " , j )
				flag = True
				break
	
		for j in range(int(ll),l):
			if(key == dataset[j]):
				print("Found key : ", key , " in index : " , j )
				flag = True
				break
		break

	if(flag == False):
		print("The key could not be found ")

l = [1,3,5,6,7,9,10]

print("Original List : ", l )

binary_search(l)

print("\n")

arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122]

print("Original List : ", arr )

binary_search(arr)


