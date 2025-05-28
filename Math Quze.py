import random
import time
def question_generator():
    a = random.randint(1,9)
    b = random.randint(1,9)

    operator_list = ['-','+','*']
    select_operator = random.choice(operator_list)
    print(f"{a} {select_operator} {b} = ?")

    if select_operator == '+':
        return a + b
    elif select_operator == '-':
        return a - b
    else :
        a * b
 
quetion_number_limit = 5
quetion_number = 0
score = 0
time_limit = 5
while quetion_number < quetion_number_limit:
    
        result = str(question_generator())
        start_time = time.time()

        user_answer = input("Enter your answer: ")
        end_time = time.time()

        time_dif = end_time - start_time

        if time_dif<time_limit:

            if user_answer == result:
                score +=1
                print(f"Perfect,{score}")
            else:
                print("Sory, your answer is wrong")
        else:
             print("you are too late ")


        quetion_number +=1
print(f"FINAL SCORE {score} out of {quetion_number_limit}")