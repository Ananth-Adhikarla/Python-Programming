"""
Text Processing. Write a program to ask the user to input a list of names, in the
format "Last Name, First Name," i.e., last name, comma, first name. Write a function
that manages the input so that when/if the user types the names in the wrong order, i.
e., "First Name Last Name," the error is corrected, and the user is notified. This
function should also keep track of the number of input mistakes. When the user is
done, sort the list, and display the sorted names in "Last Name, First Name" order.

"""
def process_name():

	print("Enter the total number of names : ")
	num = int(input())
	c = 1
	first = {}
	last = {}
	
	for j in range(0,num):
		first[j] = None
		last[j] = None

	for i in range (0,num):

		print("Please enter name : " , i )
		
		name = input()
		
		try:		
			lastName, firstName = name.split(',', 1)
		except:
			print("Wrong format... should be Last, First.")
			print("You have done this ", c ," time(s) already. Fixing input. . .")
			c += 1
			lastName, firstName = fix_name(name)
						

		first[i] = firstName
		last[i] = lastName
		
	lst1 = list(first.values())
	lst2 = list(last.values())

	#lst2.sort()

	full_name = dict(zip(lst2, lst1))
	
	print("\n\n")
	print("Sorted List by Last Name \n")

	for key in sorted(full_name):
		print(key,", ",full_name[key])

	
	print("\n")
	

def fix_name(name):

	lastName, firstName = name.split(' ', 1)

	return firstName,lastName


process_name()
