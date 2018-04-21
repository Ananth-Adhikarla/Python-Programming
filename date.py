"""

The datetime module provides data and time objects and a rich set of methods and operators. Read the documentation [here](https://docs.python.org/2/library/datetime.html). Submit the following in a file named `date.py`.

1. Use the datetime module to write a program that gets the current date and prints the day of the week.
2. Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day. Write a program that takes two birthdays and computes their Double Day.
4. For a little more challenge, write the more general version that computes the day when one person is n times older than the other.

"""

import time

from datetime import date
from datetime import datetime

def next_bday(year,month,day):
	
	today = datetime.now()

	my_bday = datetime(today.year , month , day)

	time_to_bday = ( today - my_bday)

	age = today.year - year

	print("Age of person : ", age)
		
	print("Days to birthday :", abs(time_to_bday.days))

	print("Hours to birthday :", time_to_bday.seconds // 3600 )

	print("Minutes to birthday :", time_to_bday.seconds % 3600 // 60 )

	print("seconds to birthday :", time_to_bday.seconds % 3600 )

today = date.today()

print("Current day and date ::", today.strftime("%A"),today)

next_bday(1992,12,14)








