#7-4 PROGRAMMING EXERCISE
#Design a program that asks the user to enter a series of 20 numbers
#The program should store the numbers in a list then display the following data:
#The lowest # in the list, the highest # in the list, the total of the numbers in the list, and the avg numbers in the list

# INTIALIZE EMPTY LIST TO STORE USER INPUT
numbers = []

# ASK USER FOR INPUT
print("PLEASE ENTER 20 NUMBERS:")
# LOOP 20 NUMBERS FROM USER
for count in range(1, 21): #NUMBER STARTS AT 1 INSTEAD OF 0
    while True:  # LOOP UNTIL USER ENTERS 20 NUMBERS
        try:
            num = float(input(f"Number {count}: ")) 
            numbers.append(num)  #APPEND NUMBERS INTO NUMBER LIST
            break  # EXIT IF LOOP IS INVALID
        except ValueError:
            print("ERROR. INVALID INPUT!")

# CALC THE MIN AND MAX NUMBERS IN THE LIST
lowest = min(numbers) 
highest = max(numbers)  
total = sum(numbers)    # SUM OF ALL NUMBERS ENTERED
average = total / len(numbers)  # CALC AVG NUMBERS BY DIVIDING TOTAL/ AND NUMBERS COUNTED IN LIST(20)

#DISPLAY RESULTS
print(f"LOWEST NUMBER: {lowest}")
print(f"HIGHEST NUMBER: {highest}")
print(f"TOTAL OF NUMBERS ENTERED: {total}")
print(f"AVERAGE OF NUMBERS4: {average:.2f}") 