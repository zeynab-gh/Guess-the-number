import random

name = ['ali','ahmad','sara','giti','zeynab', 'kia'] #لیست تعیرف می کنیم


select_name = random.choice(name) # قرار می دهیم select_name یک نام رندم انتخاب و داخل متغییر 

guess_count = len(select_name) #   قرار می دهیم guess_count  طول حروف رندم را در متغییر 

guessed_list = ['-'] * len(select_name) # یک لیستی می سازیم تمامی حروفش  به تعداد حرف یا کلمه که انتخاب کردیم خط تیره باشه

while guess_count > 0 : # تا زمانی که تعداد شمارش بزرگتر از صفر است کاربر می تواند حدس بزند

    guess_char = input('Enter a char: ') #دریافت ورودی
    
    if guess_char.isalpha(): #اگر کاراکتر های انتخاب شده جزء حروف انگلیسی باشد 

        if guess_char in select_name: # اگر حرفی که انتخاب کرده در لیست باشدانگاه:
            if guess_char in  guessed_list: # اگر کاراکتری که انتخاب کرده جزء حروف حدس زده ها باشد در این صورت
                print("you have guessed befor, try new character") #چک میکنیم قبلا حدس زده یانه .اگر بود این پیام را نشان میدهیم
            else: #در غیر این صورت 
              for idx, char in enumerate(select_name):# برای اینکه بتونیم هم به اندیس هم حروف دسترسی داشته باشیم از 
                                                        # استفاده می کنیم (enumerate)
                if char == guess_char: # اگر حروف موجود برابر باشه با کاراکتری باشه که کاربر انتخاب کرده
                    guessed_list[idx] = guess_char# اندیس کاراکتر را برابر اندیس حدس زده بذارید

            current_guess = " ".join(guessed_list) #با دستور جوین خط تیره هارو به هم متصل می کنیم
            print(f"Perfect => {current_guess}")# حدس شما درست است.و تعداد حدس های باقی مانده را هم نشان می دهد

            if not "-" in guessed_list:  #اگر خط  تیره ها تمام شد یعنی همه خط تیره ها پر شدند شما برنده اید
                print("You Won")
                break  # و از لوپ خارج می شود
        else:   
              guess_count -=1 #اگر حدس مون اشتباه بود از تعداد حدس هایی که می تونیم بزنیم کم کن
              print(f"Wrong => remaind guess: {guess_count}")
     
    else:
        print("Enter valid number: ")      #اگر ورودی حروف نباشه پیام خطا مبنی بر اینکه  ورودی درست وارد کنند
