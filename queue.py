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


class Queue:
  
	def __init__(self):
		self.head = None
		self.tail = None
		

	def isEmpty(self):
		return self.tail == None

	def enqueue(self,item):
		temp = Node(item)

		if(self.head == None and self.tail == None):
			temp.setNext(self.head)
			self.head = temp
			self.tail = self.head
		else:
			temp.setNext(self.tail)
			self.tail.next = temp
			self.tail = temp
			
	
		#self.tail.next = None
			
		
		#print("Tail val :  ",self.tail.getData())
		#print("Head val :  ",self.head.getData())
		


	def dequeue(self):
		

		if(self.head == None):
			return None


		else:
			current = self.head.data
			next = self.head.next

			if(next is None):
				self.head = None
				self.tail = None

			else:
				self.head = next
	
		return current

	def get_front(self):
		return self.head.data

	def get_last(self):
		return self.tail.data

	def get_next(self):
		return self.tail.next.data
		


ll = Queue()

ll.enqueue(2)
ll.enqueue(4)
ll.enqueue(6)
ll.enqueue(8)
ll.enqueue(10)
ll.enqueue(12)

print("get next",ll.get_next())
print("Front of list befoe dequeue ",ll.get_front())
print("Dequeue element ",ll.dequeue())
print("Front of list after dequeue ",ll.get_front())
print("Dequeue element ",ll.dequeue())
print("Front of list after dequeue again ",ll.get_front())


