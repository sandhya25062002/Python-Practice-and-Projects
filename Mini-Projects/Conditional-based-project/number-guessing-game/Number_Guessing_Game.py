import random

secret_number = random.randint(1, 100)

attempt_count = 0

status = True

while status :

   number = int(input("Guess the number (1 to 100 ): "))
   attempt_count += 1

   if secret_number < number :
    print("Too High ! Enter Lower number")

   elif secret_number > number:
    print("Too Low ! Enter Higher Number ")   

   else:
     print("You Won !!!")
     print("Attempt : ", attempt_count)
     break


