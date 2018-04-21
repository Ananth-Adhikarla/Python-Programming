from itertools import islice

def pager(fname):

	
	with open(fname) as fd:
		for line in islice(fd,25):
					print(line)
					print("\nPress a key to continue - Y or N :")
					status = input()
					print("\n")
					if(status == 'y' or status == 'Y'):
						continue
					else:
						break	



pager("dummy.txt")

