import math
city = input("enter a city: ")
money = float(input("enter a number: "))


if city == "sofia":
    if 0 <= money <= 500:
        realMoney = money * 0.05
    elif 500 <= money <= 1000:
        realMoney = money * 0.07
    elif 1000 <= money <= 10_000:
        realMoney = money * 0.08
    elif money > 10_000:
        realMoney = money*0.12

    print(round(realMoney, 2)) 



     
elif city == "varna":
    if 0 <= money <= 500:
        realMoney1 = money * 0.045
    elif 500 <= money <= 1000:
        realMoney1 = money * 0.075
    elif 1000 <= money <= 10_000:
        realMoney1 = money * 0.1
    elif money > 10_000:
        realMoney1 = money*0.13

    print(round(realMoney1, 2))
elif city == "plovdiv":
    if 0 <= money <= 500:
        realMoney2 = money * 0.055
    elif 500 <= money <= 1000:
        realMoney2 = money * 0.08
    elif 1000 <= money <= 10_000:
        realMoney2 = money * 0.12
    elif money > 10_000:
        realMoney2 = money*0.145
    print(round(realMoney2, 2))
else:
    print("error")