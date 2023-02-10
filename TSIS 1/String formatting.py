item=str(input("Please choose: Doner of Burger? "))
Quantity=int(input("How many? "))

price_don = 1000
price_bur = 1200
txt = "You want {0} {1}s. That'll be {2} tg"

if(item == "Doner"):
    price_don=price_don*Quantity
    print(txt.format(Quantity, item, price_don))
elif(item == "Burger"):
    price_bur=price_don*Quantity
    print(txt.format(Quantity, item, price_bur))