import random

player_name = input("Hello, whats your name: ")
print(f'grate I am '+ player_name  +  "  i want choese a number range **low** and **high**")
try:
    low = int(input("Enter low number:"))
    high = int(input("Enter high number: "))
except:
   print("Enter valid number")

a = random.randint(low,high)

count = 5

while count > 0:
    try:
        b = int (input(f"you have {count}  chance another .Enter your gesses number: "))

        if a == b:
            print("Your Win")
            break
        
        elif a > b :
            print (" <<*** Enter bigger number ***>> \n ")
        else:
            print("<<*** Enter lower number ***>>!!!\n")
        
        count -=1
       
        if count == 0:
            print("game over")

    except:
        print("Enter valid number: ")


    
