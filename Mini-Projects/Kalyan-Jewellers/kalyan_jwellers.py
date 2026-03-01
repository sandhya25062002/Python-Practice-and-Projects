print("")

print("----- ---------------kalyan jwellers---------------------")
name = (input("enter your name : "))
gender = (input("enter gender (m / f): "))
age = int(input("enter age : "))

print("")

product = input("enter product : ")
product_gram = int(input("enter product gram : "))
current_gold_rate = 11190
print(f"current gold rate (1 gram ) : 11,190")

print("-------------------------------------------------------")

total_gold_rate = product_gram * current_gold_rate
print(f"TOTAL GOLD RATE : {total_gold_rate}")

print("")

making_charges = 845

print("making charges (1 gram ): 845")

total_making_charge = product_gram * making_charges

print(f"TOTAL MAKING CHARGES : {total_making_charge}")

print("-----------------------------------------------------------")

total_amount= total_gold_rate + total_making_charge

print("TOTAL AMOUNT : ", total_amount)


if gender == 'm':
    if age >= 65 : 
        if total_amount >= 200000 and total_amount < 300000:
         print("discount : 20 %")
         discount = total_gold_rate * 20 / 100
         net_amount  = total_amount - discount

         print("-------------------------------------------")
         print(f"your discount is {discount} ")

         print("-------------------------------------------")

         print(f"net payable amount : {net_amount}")

        elif total_amount >= 300000 and total_amount < 500000:
           print("discount : 30 %")
           discount = total_gold_rate * 30 /100
           net_amount = total_amount - discount

           print("-------------------------------------")
           print(f"your discount is {discount}")

           print("----------------------------------------")

           print(f"net payable amount : {net_amount}")

         
        elif total_amount >= 500000:
           print("discount : 35%")
           discount = total_gold_rate * 35 /100
           net_amount = total_amount - discount

           print("-----------------------------------------")
           print(f"your discount is {discount}")

           print("------------------------------------------")

           print(f"net payable amount : {net_amount}")

    else :
        if total_amount >= 200000 and total_amount < 300000:
           print("discount : 10%")
           discount = total_gold_rate * 10 /100
           net_amount = total_amount - discount

           print("-----------------------------------------")
           print(f"your discount is {discount}")

           print("----------------------------------------")

           print(f"net payable amount : {net_amount} ")

        elif total_amount >= 300000 and total_amount < 500000:
           print("discount : 20% ")
           discount = total_gold_rate * 20 / 100
           net_amount = total_amount - discount

           print("----------------------------------------")
           print(f"your discount is {discount}")

           print("----------------------------------------")
           print(f"net payable amount : {net_amount}")
           
        elif total_amount >= 500000:
           print("discount : 25%")
           discount = total_gold_rate * 25 / 100
           net_amount = total_amount - discount

           print("----------------------------------------")
           print(f"your discount is : {discount} ")

           print("----------------------------------------")

           print(f"net payable amount : {net_amount}")
elif gender == 'f':
   if age > 65:
      if total_amount >= 200000 and total_amount < 300000:
         print("discount : 25%")
         discount = total_gold_rate * 25 / 100
         net_amount = total_amount - discount

         print("-----------------------------------------")
         print(f"your discount is : {discount}")

         print("----------------------------------------")
         print(f"net payable amount : {net_amount}")

      elif total_amount >= 300000 and total_amount < 500000:
         print("discount : 35%")
         discount = total_gold_rate * 35 / 100
         net_amount = total_amount - discount

         print("-----------------------------------------")
         print(f"your discount is : {discount}")

         print("-----------------------------------------")
         print(f"net payable amount : {net_amount}")
      elif total_amount >= 500000:
         print("discount : 40%")
         discount =  total_gold_rate * 40 / 100
         net_amount = total_amount - discount

         print("-----------------------------------------")
         print(f"your discount is : {discount}")
         print("-----------------------------------------")
         print(f"net payable amount : {net_amount}")
   else:
      if total_amount >= 200000 and total_amount < 300000:
         print("discount : 15%")
         discount = total_gold_rate * 15 / 100
         net_amount = total_amount - discount

         print("------------------------------------------")
         print(f"your discount is : {discount}")
         print("------------------------------------------")
         print(f"net payable amount : {net_amount}")
      elif total_amount >= 300000 and total_amount < 500000:
         print("discount : 25%")
         discount = total_gold_rate * 25 / 100
         net_amount = total_amount - discount

         print("-------------------------------------------")
         print(f"your discount is {discount}")
         print("--------------------------------------------")
         print(f"net payable amount : {net_amount}")
      elif total_amount >= 500000:
         print("discount : 30%")
         discount = total_gold_rate * 30 / 100
         net_amount =  total_amount - discount

         print("----------------------------------------------")
         print(f"your discount is : {discount}")
         print("-----------------------------------------------")
         print(f"net payable amount : {net_amount}")
else :
   print("invalid input ")   

               
  

      

           
    
    
        

        




