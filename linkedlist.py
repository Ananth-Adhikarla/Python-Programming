"""
LINKED LISTS
"""

class Node:

	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):	
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class List:

	def __init__(self):
		self.head = None
		

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
			return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
			
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())

	def print_ll(self):
		current = self.head
		while current != None:
			print(current.data)
			current = current.next


ll = List()
ll.add(0)
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
print(ll.search(1))
ll.print_ll()

