def createFile(fname):

	fd = open(fname , "w+")

	print("Enter some data to your file : ")

	while(True):
		
		line = input()
		if(line == 'exit'):
			break		
		else:		
			fd.write(line) 
			fd.write("\n")			
	fd.close()

	print("\n\n\n\n")
	print("Data stored on file : \n")

	with open(fname, "r+") as f:
		print(f.read())


createFile("sample.txt")
