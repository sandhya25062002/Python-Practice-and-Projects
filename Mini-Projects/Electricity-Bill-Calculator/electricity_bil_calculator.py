print("")

name = input("enter your name : ")

use_unit = int(input("enter you used unit in this month :  "))

rate1 = 5  #  0 to 100 unit
rate2 = 7  #  101 to 200 unit
rate3 = 10 #  201 to 300 unit
rate4 = 15 #  above 300 unit

fixed_meter_charge = 50 
peak_hour_unit = int(input("enter peak hour used unit : "))
late_payment = input("is your payment delay ? (yes / no) : ")


if use_unit >= 0 and peak_hour_unit >= 0:
    if use_unit <= 100:
        amount = use_unit * rate1
        msz = "low consumption"
    elif use_unit <= 200:
        amount = (100 * rate1 )  + (use_unit - 100) * rate2
        msz = "medium consumption"
    elif use_unit <= 300:
        amount = (100 * rate1)  + (100 * rate2) + (use_unit - 200) * rate3
        msz = "medium consumption"
    else : 
        amount = (100 * rate1)  + (100 * rate2) +  (100 * rate3) + (use_unit - 300) * rate4
        msz = "high consumption"

        # -- Applies a 10% surcharge if total units exceed 500 units.

    if use_unit > 500 : 
        surcharge =  amount * 10 / 100
    else :
        surcharge = 0

        # -- Provides a 5% discount if consumption is below 50 units as a low-usage incentive.

    if use_unit < 50 :
        discount =  amount * 5 / 100
    else :
        discount = 0    
       
        """ Includes extra charges for peak-hour consumption: ₹2/unit for units consumed during 
            peak hours above 50 units."""
        
    if peak_hour_unit > 50 :
        extra_charge = (peak_hour_unit - 50 ) * 2
    else :
        extra_charge = 0

      # optionally add a late payment penalty of ₹100 if payment is delayed.


    if late_payment == "yes":
        late_payment_charge = 100 
    elif late_payment == "no":
        late_payment_charge = 0 
    else:
        print("invalid input ! please enter valid input ") 
              
    
        """ Calculates and displays a final formatted bill, showing total amount, surcharge, discounts, 
                    and fixed charges."""


    total = amount + fixed_meter_charge + surcharge + extra_charge + late_payment_charge - discount
 
    print("------------ ELECTRICITY BILL CALCULATOR -----------------")

    print(f"name is : {name}")
    print(f"consumed unit : {use_unit}")
    print(f"base amount : {amount}")
    print(f"fixed meter charge : {fixed_meter_charge}")
    print(f"peak hour extra charge : {extra_charge}")
    print(f"surcharge (if any) : {surcharge}")
    print(f"discount (if any) : {discount}")
    print(f"late payment panelty : {late_payment_charge}")

    print("-------------------------------------------------------------")

    print(f"TOTAL PAYABLE AMOUNT : {total}")
    print(f"consumption type : {msz}")

    print("")

    print ("THANK YOU -----")

else :
    print("invalid input !  negetive numbers not allowed . please enter positive numbers")




   