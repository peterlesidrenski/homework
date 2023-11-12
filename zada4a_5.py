place = input("enter place: ")
product = input("enter product: ")
quantity = float(input("enter quanity: "))

if place == "School":
    if product.lower() == "coffee":
        print(quantity * 0.50)
    elif product.lower() == "water":
        print(quantity * 0.80)
    elif product.lower() == "beer":
        print(f"{(quantity * 1.20):.1f}")
    elif product.lower() == "sweets":
        print(f"{(quantity * 1.45):.1f}")
    elif product.lower() == "peanuts":
        print(quantity * 1.60)
    else:
        print("There is no such product!")
elif place == "Dormitory":
    if product.lower() == "coffee":
        print(quantity * 0.40)
    elif product.lower() == "water":
        print(quantity * 0.70)
    elif product.lower() == "beer":
        print(quantity * 1.15)
    elif product.lower() == "sweets":
        print(quantity * 1.30)
    elif product.lower() == "peanuts":
        print(quantity * 1.50)
    else:
        print("There is no such product!")
elif place == "Bus-station":
    if product.lower() == "coffee":
        print(quantity * 0.45)
    elif product.lower() == "water":
        print(quantity * 0.70)
    elif product.lower() == "beer":
        print(quantity * 1.10)
    elif product.lower() == "sweets":
        print(quantity * 1.35)
    elif product.lower() == "peanuts":
        print(quantity * 1.55)
    else:
        print("There is no such product!")
else:
    print("There is no such place!")