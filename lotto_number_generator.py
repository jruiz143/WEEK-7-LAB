#7-2 Programming Exercises
#Design a program that generates a 7 digit lottery
#number. The program should generate seven random numbers,
#each in the range of 0 through 9, and assign each number to 
#a list element. Then write another loop that displays the contents of the list

import random

def main():
    lottery_number = []
    
    # GENERATE 7 RANDOM NUMBERS IN THE LIST
    for I in range(7):  
        lottery_number.append(random.randint(0, 9))  #APPEND RANDOM NUMBERS TO LOTTERY NUMBER LIST

    # DISPLAY LOTTERY NUMBER
    for numbers in lottery_number: 
        print(numbers)

main()