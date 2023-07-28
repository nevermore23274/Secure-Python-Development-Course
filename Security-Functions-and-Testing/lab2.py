# Import(s)
from datetime import date
import random
import string
import math

# Menu variable(s)
MENU_INCREMENT = 0

while MENU_INCREMENT != 6:
    print("\n" +"*** Welcome to the Week 2 Lab ***")
    print("1.) Generate Secure Password")
    print("2.) Calculate and Format a Percentage")
    print("3.) How many days from today until July 4, 2025?")
    print("4.) Use the Law of Cosines to calculate the leg of a triangle")
    print("5.) Calculate the volume of Right Circular Cylinder")
    print("6.) Exit Program")

    user_input = input("Enter a choice: ")
    if user_input == '1':
        passwd_len = int(input("Length of the password: "))
        passwd_nums = int(input("0 for no numbers, 1 for numbers:  "))
        passwd_upper = int(input("0 for no uppercase letters, 1 for uppercase letters:  "))
        passwd_lower = int(input("0 for no lowercase letters, 1 for lowercase letters:  "))
        passwd_specs = int(input("0 for no special characters, 1 for special characters:  "))
        FINAL_PASSWD = ""
        passwd_dict = []

        if passwd_nums == 1:
            # Generate between 6 and 20 random integers to place in list
            for i in range(random.randint(6, 20)):
                passwd_digit_set = random.choice(string.digits)
                passwd_dict.append(passwd_digit_set)
        else:
            print("invalid input")
            continue

        if passwd_upper == 1:
            # Generate between 6 and 20 random uppercase letters to place in list
            for i in range(random.randint(6, 20)):
                passwd_upper_set = random.choice(string.ascii_uppercase)
                passwd_dict.append(passwd_upper_set)

        if passwd_lower == 1:
            # Generate between 6 and 20 random lowercase letters to place in list
            for i in range(random.randint(6, 20)):
                passwd_lower_set = random.choice(string.ascii_lowercase)
                passwd_dict.append(passwd_lower_set)

        if passwd_specs == 1:
            for i in range(random.randint(6, 20)):
                # Generate between 6 and 20 random symbols to place in list
                passwd_special_set = random.choice(string.punctuation)
                passwd_dict.append(passwd_special_set)

        for i in range(passwd_len):
            FINAL_PASSWD += random.choice(passwd_dict)

        print("\n" + "Secure Password---> ", FINAL_PASSWD + "\n")

    elif user_input == '2':
        numerator = float(input("Enter numerator: "))
        denomenator = float(input("Enter denomenator: "))
        decimal = int(input("Enter the number of decimal points: "))
        percentage = numerator/denomenator * 100
        percentage = round(percentage, decimal)
        print('\n' + f"Percentage value: {percentage}%" + '\n')

    elif user_input == '3':
        current_day = date.today()
        proj_day = date(2025, 7, 4)
        delta = proj_day - current_day
        print('\n' + f"Total number of days are {delta.days}" + '\n')

    elif user_input == '4':
        a = int(input("Enter first side length: "))
        b = int(input("Enter second side length: "))
        ang = int(input("Enter the angle: "))
        c = round(math.sqrt(a*a + b*b - 2*a*b*math.cos(math.pi/180*ang)), 2)
        print('\n' + f"The leg of the triangle is {c}" + '\n')

    elif user_input == '5':
        r = int(input("Enter the radius: "))
        h = int(input("Enter the height of cylinder: "))
        cyl_volume = round((math.pi*r*r)*h, 4)
        print('\n' + f"Cylinder Volume: {cyl_volume}" + '\n')

    elif user_input == '6':
        print("\n" + "Thank you for your time, goodbye.")
        break
    else:
        print("\n" + "Invalid input, please use values 1 through 6 for menu options.")
