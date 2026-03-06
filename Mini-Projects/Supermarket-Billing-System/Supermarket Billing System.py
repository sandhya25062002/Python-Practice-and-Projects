print("")

# product catogary 

sugar_price = 53           # sugar rs 53 pr kg
chocolate_price = 10      # 10rs per chocolate
mobile_price = 1500        # 1500rs per mobile
laptop_price = 70000       # 70000rs per laptop
greentea_price = 45        # 45rs per greentea packet

 # gst as per item food item 5 % tax and non food item 12 % tax

food_item_tax = 5
non_food_item = 12



name =  input("enter your name : ")

choice = input("enter item name : ").lower()

quantity = int(input("enter quantity : "))
if quantity <= 0:
    print("Invalid quantity")
    exit()

membership = input(" membership card (gold/ silver / none ) : ").lower()

home_delivery = input("if you want home delivery service (yes / no ): ").lower()

if choice == "sugar":
    amount = sugar_price * quantity 
    gst = amount * food_item_tax / 100

elif choice == "chocolate":
    amount = chocolate_price *  quantity
    gst = amount * food_item_tax / 100

elif choice == "mobile":
    amount =  mobile_price * quantity
    gst = amount * non_food_item / 100

elif choice == "laptop":
    amount =  laptop_price * quantity
    gst = amount * non_food_item / 100

elif choice == "greentea":
    amount = greentea_price * quantity    
    gst = amount * food_item_tax / 100

else : 
      print("invalid input ! please enter valid item") 
      exit()
    

    # membership discount     


if membership == "gold":
    discount = amount * 10  / 100
 
elif membership == "silver":
    discount = amount * 5 / 100

else : 
    discount = 0  

    # home delivery charge      

if home_delivery == "yes":
    extra_charge = 40 
else :
    extra_charge = 0    

total = amount  + gst  + extra_charge - discount

print("")

print("-------------------- SUPER MARKET BILLING SYSTEM ------------------------")

print(f"name :  {name}")
print(f"item : {choice}")
print(f"quantity : {quantity}")
print(f"basic amount  : {amount}")
print(f"gst : {gst}")
print(f"discount : {discount}")
print(f"home delivery (if any ) : {extra_charge}")

print("------------------------------------------------------------------------")

print(f"TOTAL PAYABLE AMOUNT : {total}")


print("----------------------------------------------------------")

print("THANK YOU ! VISIT AGAIN ")






 