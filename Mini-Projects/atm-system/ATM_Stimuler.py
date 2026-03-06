user_name_db = 123
password_db = 12345

balance =  10000

print(" !!!! Welcome !!!!!")
username =  int(input("Enter Username : "))
password = int(input("Enter password : "))

if username != user_name_db or password != password_db:
    print("Error !! invalid credentials !! Please Enter Valid Username and Password ")

else:

    print(" ---------------------- Menu ------------------------- ")
    menu = """
   1. View balance
   2. Deposit money
   3. Withdraw money
   4. Exit

"""
    
    status = True

    while status :
      
      print(menu)

      user_choice = int(input("Enter choice : "))

      # View balance

      if user_choice == 1:
       print(f"Your Current Balance : {balance}")

      # Deposit Money

      elif user_choice == 2:
       print(f"Current balance : {balance}")
       deposit_money = int(input("Enter Deposit money : "))

       if deposit_money <= 0 :
        print("Invalid amount")

       else:
        balance += deposit_money
        print(f"Successfully Deposit : {deposit_money} ")
        print(f"\ncurrent balance : {balance}")

      # withdraw Money

      elif user_choice == 3:
       print(f"current balance : {balance}") 
       withdraw_money = int(input("Enter withdraw Money : "))

       if withdraw_money > balance:
        print("Error !! insufficient fund ")

       elif withdraw_money <= 0:
        print("Invalid amount") 

       else:
        balance -= withdraw_money
        print(f"successfully withdraw : {withdraw_money}")   
        print(f"\ncurrent balance : {balance}") 

        # exit

      elif user_choice == 4:
        print("Thank you for Using ATM ")
        status = False

      else:
        print("Invalid Choice. Try Again")  






