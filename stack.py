"""
STACKS
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




class Stack:

	def __init__(self):
		self.head = None
		
	
	def isEmpty(self):
		return self.head == None

	def push(self, item):

		temp = Node(item)
		temp.next = self.head
		self.head = temp
		#print(self.head.data)

	def pop(self):
		
		temp = self.head.data
		self.head = self.head.next
		return temp
		

				
	
		
	def peek(self):
		
		count = 0

		current = self.head

		while(current is not None):
			count += 1
			current = current.next
			
		return count

	def print_s(self):
		
		current = self.head

		while(current is not None):
			print(current.data)
			current = current.next

	def isEmpty(self):
		
		if(self.head == None):
			return None

		else:
			return 'Stack is NOT EMPTY'

    


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Size of the current stack before pop",s.peek())

print("First pop ",s.pop())

print("Size of the current stack after 1 pop",s.peek())

print("Second pop ",s.pop())

print("Size of the current stack after 2 pop",s.peek())

print("Second pop ",s.pop())

print("Size of the current stack after 2 pop",s.peek())

print("Second pop ",s.pop())

print("Size of the current stack after 2 pop",s.peek())

print(s.isEmpty())

print("Second pop ",s.pop())

print("Size of the current stack after 2 pop",s.peek())

print(s.isEmpty())

