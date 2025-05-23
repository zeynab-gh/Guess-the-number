import random

try:
    low = int(input("Enter low number:"))
    high = int(input("Enter high number: "))
except:
   print("Enter valid number")

a = random.randint(low,high)

count = 5

while count > 0:
    try:
        b = int (input("Enter your gesses number: "))

        if a == b:
            print("Your Win")
            break
        
        elif a > b :
            print (" Enter bigger number :  ")
        else:
            print("Enter lower number")
        
        count -=1
        print(f"you have {count}  chance another")
        if count == 0:
            print("game over")

    except:
        print("Enter valid number: ")


    
