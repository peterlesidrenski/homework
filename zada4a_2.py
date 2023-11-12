day = (input("enter day: "))
day_of_week = day.casefold ()
if day_of_week == "monday":
   print ("study day")
elif day_of_week == "tuesday":
   print ("study day")
elif day_of_week == "wednesday":
   print ("study day")
elif day_of_week == "thursday":
   print ("study day")
elif day_of_week == "friday":
   print ("study day")
elif day_of_week == "saturday":
   print ("weekend")
elif day_of_week == "sunday":
   print ("weekend")
else:
   print ("ERROR")