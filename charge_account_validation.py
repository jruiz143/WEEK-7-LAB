#7-5 Programming Exercises 
#Write a program that reads the contents of the file (charge_accounts.txt) into a list. 
#The program should then ask the user to enter a charge account number
#The program should determine whether the number is valid by searching
#For it in the list. If the number is in the list, the program should display
#A message indicating the number is valid. If the number is not the list, the program should display a message
#Indicating the number is invalid. 

# CREATE EMPTY LIST FOR CHARGE ACCOUNTS NUMBERS FOR USER INPUT
charge_accounts = []

# OPEN FILE AND READ
try:
    with open('charge_accounts.txt', 'r') as file:  
        #LOOP AND READ THROUGH EACH LINE IN FILE
        for line in file:
            charge_accounts.append(line.strip()) #REMOVE WHITESPACE AND APPEND IN CHARGE ACCOUNT LIST
except:
    print("ERROR.")

# GET USER INPUT AND CHECK CHARGE ACCOUNTS
if charge_accounts:
    user_input = input("Please enter a charge account number: ")

    # CHECK IF CHARGE ACCOUNT NUMBER IS VALID
    if user_input in charge_accounts:
        print("CHARGE ACCOUNT NUMBER IS VALID.")
    else:
        print("CHARGE ACCOUNT NUMBER IS INVALID.")
else:
    print("ERROR")#HANDLE EXCEPTIONS