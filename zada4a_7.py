hour = int(input("enter hour: "))
day_of_week = input("enter a day: ")
if day_of_week == "sunday":
        print ("Closed")
elif 13 <= hour < 15:
        print ("Closed")
elif 7 <= hour < 17 and day_of_week == "monday" or "tuesday" or "wednesday" or " thursday" or "friday" or "saturday":
        print ("Open")
else:
        print ("Closed")