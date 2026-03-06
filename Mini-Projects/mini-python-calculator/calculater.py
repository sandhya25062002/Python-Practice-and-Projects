print("--------Mini Calculator---------------")

status = True

while status:
    try:
        num1 = float(input("Enter number 1 : "))
        num2 = float(input("Enter number 2 : "))
    except:
        print("Invalid number ! Try again")  
        continue

    menu = """

      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Exit

       """
    print(menu)

    choice = (input("Enter Choice : "))

    if choice == "1":
        print("Result :", num1 + num2)

    elif choice == "2":
        print("Result :", num1 - num2)

    elif choice == "3":
        print("Result",num1 * num2)  

    elif choice == "4":
        if num2 == 0 :
            print(" Error ! can not devide by Zero")   
        else:
            print("Result", num1/num2)    

    elif choice == "5":
        print("calculator Close !")
        status = False

    else:
        print("Invalid Choice ! Please Select 1-5")





