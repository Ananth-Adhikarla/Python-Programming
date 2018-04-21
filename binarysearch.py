"""
Binary Search
"""

#import wordlist.txt

def binary_search(dataset):
	
	key = input("Enter the key to search in list	")
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



ll = []

with open("wordlist.txt","r") as this_file:
	for word in this_file:
		ll.append(word.strip("\n"))	
		


#print(ll)
binary_search(ll)
