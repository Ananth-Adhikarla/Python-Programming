import datetime

def find_double_day(bday1, bday2):
 
    person1 = datetime.date(*bday1)
    person2 = datetime.date(*bday2)

    age_diff = -(person1 - person2)

    p1 = int(age_diff.days)
    p2 = 0

    while (p2 * 2 != p1):
        p1 += 1
        p2 += 1

    date_at_twice_age = person2 + datetime.timedelta(days=p2)
    print (date_at_twice_age, "\n", "person 1 was %d days old, and person 2 was %d days old" % (p1, p2))



find_double_day((1992,12,14), (1992,12,14))
