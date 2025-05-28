import random

name = ['ali','ahmad','sara','giti','zeynab', 'kia']
selected_name =random.choice(name)

guess_count = len(selected_name)
guess_list = ['_'] * len(selected_name)

while guess_count > 0:
    guess_char = input("Enter a char: ")
    if guess_char.isalpha():
        if guess_char in selected_name:
            if guess_char in guess_list:
                print("you have guessed befor, try new character")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guess_char:
                     guess_list[idx] = guess_char
            current_guess = " ".join(guess_list) 
            print(f"Perfect => {current_guess}")

            if not "-" in guess_list:   
                print("You Won")
                break

        else:
                guess_count -=1
                print(f"Wrong => remaind guess: {guess_count}")


    else:
        print("Enter valid char")