# Text Process
"""
Text Processing. Determine the total number of vowels, consonants, and words
(separated by spaces) in a text sentence. Ignore special cases for vowels and
consonants such as "h," "y," "qu," etc. Extra credit: create code to handle those
special case.
"""

def process(text):
	
	txt = list(text)
	tex = text.split(" ")
	
	flag = True

	vowel = ['a','e','i','o','u']

	count_vowel = 0
	count_consonant = 0
	count_words = 0

	for i in txt:
		if( i in vowel ):
			count_vowel += 1
		elif(i not in vowel):
			if( i == 'h' or i == 'y' or i == 'qu'):
				continue
			else:
				count_consonant += 1
	
	for j in tex:
		if( j != ','):
			count_words += 1
		
	
	print("size of text : ", len(tex))
	print("Count vowel ", count_vowel)
	print("Count consonant ", count_consonant)
	print("Count words ", count_words)

process("This")	
