
def compare(fname1,fname2):

	fd1 = open(fname1,"r")
	fd2 = open(fname2,"r")

	lines1 = fd1.readlines()

	with open(fname1,"r") as file1:
		with open(fname2, "r") as file2:
			same1= set(file1).difference(file2)
			same2 = set(file2).difference(file1)



	for i,lines2 in enumerate(fd2):
	    if lines2 != lines1[i]:
	        print ("line ", i, " in File2 is different from File1 \n")
	      #  print (lines2)
	    else:
	        continue

	list1 = str(same1)
	list2 = str(same2)

	list1.split()
	list2.split()

	len1 = len(list1)
	len2 = len(list2)
	
	print(len1)
	print(len2)


			


compare("random.txt" , "random2.txt")		



