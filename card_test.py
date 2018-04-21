"""
Card test

	self.card_number = "the card number"
  		self.card_type = "a string"
  		self.valid = "a boolean"
"""
class CreditCard:
	def __init__(self, card_number):
  		self.card_number = card_number
  		self.card_type = self.determine_card_type()
  		self.valid = self.validate()

#Create and add your method called `determine_card_type` to the CreditCard class here:
	def determine_card_type(self):
		if(int(self.card_number[0]) == 4):
			print("Valid Visa Card")
			return 'VISA'
		elif( int(self.card_number[0] ) == 5  and ( int(self.card_number[1] ) == 1 or  int(self.card_number[1]) == 2 or int(self.card_number[1] ) == 3 or  int(self.card_number[1]) == 4 or 
			int(self.card_number[1] ) == 5  ) ):
			print("Valid Master Card")
			return 'MASTERCARD'
		elif( ( int(self.card_number[0] ) == 3 and  int(self.card_number[1]) == 4 ) or ( int(self.card_number[0] ) == 3 and  int(self.card_number[1]) == 7)  ):
			print("Valid Amex")
			return 'AMEX'
		elif(  int( self.card_number[0] ) == 6  and int(self.card_number[1]) == 0 and int(self.card_number[2]) == 1 and int(self.card_number[3])  == 1 ):
			print("Valid Discover Card")
			return 'DISCOVER'
		else:
			print("Not Valid Card Type")
			return 'INVALID'
		pass

#Create and add your method called `check_length` to the CreditCard class here:
	def check_length(self):
		
		#x,y = self.determine_card_type()
		if( self.card_type == 'VISA' or self.card_type == 'MASTERCARD' or self.card_type == 'DISCOVER' ):
			if( len(self.card_number) == 16 ):
				print("Valid length of 16")			
				return True
			else:
				print("Not Valid L")
				return False

		elif( self.card_type == 'AMEX'):
			if( len(self.card_number) == 15 ):
				print("Valid length of 15")			
				return True
			else:
				print("Not Valid L")
				return False
		else:
			return False
		pass



#Create and add your method called 'validate' to the CreditCard class here:
	def validate(self):


		x = self.determine_card_type()
		y = self.check_length()

		card_num_reversed = ''

		print("Length test : " , y)
		
		if( y == True ):
			for i in reversed(self.card_number):
				card_num_reversed += i
		

		print("\n\nOriginal Number\n\n")
		print(self.card_number , end = '')

		print("\n\n")
		
		print(card_num_reversed)
		
		count = []
		check_sum = 0
		check_sum1 = 0 
		count2 = []
		for i,j  in enumerate(card_num_reversed):
			if( i % 2 == 1 ):
				count.append(int(j) * 2 )
			else:
				count.append(int(j))
		
		for i in count:
			if( len(str(i)) == 2 ):
				for j , k in enumerate(str(i)):	
					count2.append((k))
					
		for i in count:
			if( len(str(i)) == 2 ):	
				count.remove((i))
					
		for i in count2:
			count.append(i)
	
		
		print("count1 : " , count , end = '' )
		print("\n")
	
		for i in count:
			check_sum += int(i)

		print("Check sum  :" ,check_sum)
		
		print("\n")
		
		if( ( check_sum % 10 ) == 0 ):
			print("Card checksum is valid")
			return True
		else:
			print("Card checksum is not valid")
			self.card_type = 'INVALID'
			return False

		pass


