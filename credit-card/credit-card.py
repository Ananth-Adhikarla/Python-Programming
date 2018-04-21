# Author: Cody Hess
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
			return 'VISA'
		elif( int(self.card_number[0] ) == 5  and ( int(self.card_number[1] ) == 1 or  int(self.card_number[1]) == 2 or int(self.card_number[1] ) == 3 or  int(self.card_number[1]) == 4 or 
			int(self.card_number[1] ) == 5  ) ):
			return 'MASTERCARD'
		elif( ( int(self.card_number[0] ) == 3 and  int(self.card_number[1]) == 4 ) or int(self.card_number[0] ) == 3 and  int(self.card_number[1]) == 7 ):
			return 'AMEX'
		elif(  int( self.card_number[0] ) == 6  and int(self.card_number[1]) == 0 and int(self.card_number[2]) == 1 and int(self.card_number[3])  == 1 ):
			return 'DISCOVER'
		else:
			return 'INVALID'
		pass

#Create and add your method called `check_length` to the CreditCard class here:
	def check_length(self):
		
		#x,y = self.determine_card_type()
		if( self.card_type == 'VISA' or self.card_type == 'MASTERCARD' or self.card_type == 'DISCOVER' ):
			if( len(self.card_number) == 16 ):
				return True
			else:
				self.card_type = 'INVALID'
				return False

		elif( self.card_type == 'AMEX'):
			if( len(self.card_number) == 15 ):		
				return True
			else:
				self.card_type = 'INVALID'
				return False
		else:
			return False
		pass


#Create and add your method called 'validate' to the CreditCard class here:
	def validate(self):

		y = self.check_length()

		card_num_reversed = ''
		
		if( y == True ):
			for i in reversed(self.card_number):
				card_num_reversed += i			
		else:
			self.card_type = 'INVALID'
			return False

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

		for i in count:
			check_sum += int(i)

		print(check_sum)
		
		print("\n")
		
		if( ( check_sum % 10 ) == 0 ):
			return True
		else:
			self.card_type = 'INVALID'
			return False

		pass

#do not modify assert statements


cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
