age = int(input("enter a number: "))
gender = input("enter gender m or f: ")
if age >= 16 and gender == "m":
    print ("mr.")
elif age < 16 and gender == "m":
    print ("Master")
elif age >= 16 and gender == "f":
     print ("Ms.")
elif age < 16 and gender == "f":
    print ("Miss")
