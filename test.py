
with open("random.txt","r") as file:
	for line in file:
		print("Read Line ",line)
		
		
print("Current pos", line.tell() )
#print("Current pos" , pos)

