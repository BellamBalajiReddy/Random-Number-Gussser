import random

top_of_range = input("type a number")

if top_of_range.isdigit():
    top_of_range =int(top_of_range)

    if top_of_range <= 0:
        print ("Enter a number greaater than zero")
        quit()
else:
   print("please type a number next time")
   quit()  
random_number= random.randint(0,top_of_range)
guesses =0

while True:
    guesses += 1
    user_guess = input("Make a gusses")
    if user_guess.isdigit():
       user_guess =int(user_guess)
    else:
        print("please enter next time")
        continue

    if user_guess ==random_number:
         print("YOU GOT THE VALUE")
         break
    elif user_guess >random_number:  
          print("you entered a number greaater than the given number")
    else:
        print("you enterend less than the number")   
        
print("you got the correct gusses in ", guesses , "chanches")

   

