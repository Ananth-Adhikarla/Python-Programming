"""
Please submit the following in a file named `anagram.py`.

1. An anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Uppercase and lowercase letters are considered the same and you may add white spaces wherever you want. For example, the name "Tom Marvolo Riddle" can be rearranged the sentence "I am Lord Voldemort". Now, given two strings a and b, write a function `isAnagram(a, b)` which returns True if a and b are anagrams of one another, and False otherwise. You may not use any sorting functionality.

"""

#funtion isAnagram(a,b) defined here it returns True is a and b are anagrams of each other

def isAnagram(a,b) :

	a = a.lower()
	b = b.lower()

	print(list(a))
	a = a.strip()
	b = b.strip()

	print(a)

	a = a.replace(" ","")
	b = b.replace(" ","")

	print(a)
	
	x = list(a)
	y = list(b)

	p = len(x)
	q = len(y)

	print("Word A is ",x)
	print("\nWord B is ",y)
	print("\nLength of A is ",p , "Length of B is",q)

	seen =  set()
	list3 = set()

	anagram = False

	if(p != q):
		print("A is not a Anagram of B")
		return anagram;
	else:
		for element in x:	
			seen.add(element)
		
		for element in y:
				seen.add(element)
		
		for element in seen:
			if(element  in x and element  in y ):
				list3.add(element)

		for element in seen:
			if(element in list3 and element in seen):
				anagram = True
			else:
				anagram = False		
			

		print("List3 = ",list3 , "\n")		
			
		return anagram



print("Test Case 1 \n\n")
print(isAnagram("Tom Marvolo Riddle" , "I am Lord Voldemort"))

print("-------------------------------------------------------------------------------")
print("Test Case 2 \n\n")
print(isAnagram("Hello" , "World"))

print("-------------------------------------------------------------------------------")
print("Test Case 3 \n\n")
print(isAnagram("ANANTH" , "HTNANA"))

print("-------------------------------------------------------------------------------")
print("Test Case 4 \n\n")
print(isAnagram("Batman" , "Superman"))
