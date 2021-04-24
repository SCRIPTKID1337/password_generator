import random
import pyperclip

while True:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*<>?"
    all = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample (all,length))
    print ("\nyour password is :- "+password)
    print('\nchoose a option:-\n\n1.Copy\n2.Re-Generate\n3.Exit')
    
    user_input = input("\ntype 1 or 2 or 3 :- ")
    if user_input == "1":
        pyperclip.copy(password)
        break
    elif user_input == "2":
        password = "".join(random.sample (all,length))
        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # print('\nchoose a option:-\n1.Copy\n2.Re-Generate')
    elif user_input == "3":
        break
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\nchoose a right option***")
        



