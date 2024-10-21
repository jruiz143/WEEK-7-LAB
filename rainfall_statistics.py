#7-3 PROGRAMMING EXERCISE Rainfall Statistics
#Design a program that lets the user enter the total rainfall for each of 12 months
#Into a list. The program should calculate and display the total rainfall for the year, 
#The avg monthly rainfall, the months with the highest and lowest amounts.

# Rainfall Statistics
# Design a program that lets the user enter the total rainfall for each of 12 months
# into a list. The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, and the months with the highest and lowest amounts.

# GLOBAL VARIABLES
rainfall_per_month = 12
months_of_year = ['JAN', 'FEB', 'MARCH', 'APR', 
    'MAY', 'JUNE', 'JUL', 'AUG', 
    'SEPT', 'OCT', 'NOV', 'DEC']

def main(): 
    # INTIALIZE LIST TO STORE RAINFALL DATA
    rainfall = [0] * rainfall_per_month
    
    # RECEIVE USER INPUT FOR RAINFALL
    for index in range(rainfall_per_month):
        rainfall[index] = float(input(f'ENTER RAINFALL FOR {months_of_year[index]}: '))
    
    # CALC TOTAL RAINFALL
    total_rainfall = sum(rainfall)
    
    # CALC AVG RAINFALL 
    average_rainfall = total_rainfall / rainfall_per_month
    
    # FIND HIGHEST AND LOWEST RAINFALL MONTH
    highest_rainfall = rainfall[0]
    lowest_rainfall = rainfall[0]
    month_highest = 0  # INTIALIZE MONTH
    month_lowest = 0   

    for month in range(rainfall_per_month):
        if rainfall[month] > highest_rainfall:
            highest_rainfall = rainfall[month]
            month_highest = month  

        if rainfall[month] < lowest_rainfall:
            lowest_rainfall = rainfall[month]
            month_lowest = month  

    # DISPLAY RESULTS
    print(f"TOTAL RAINFALL OF THE YEAR: {total_rainfall:.2f} inches.")
    print(f"AVERAGE MONTHLY RAINFALL: {average_rainfall:.2f} inches.")
    print(f"THE MONTH OF{months_of_year[month_highest]} HAD THE HIGHEST RAINFALL OF {highest_rainfall:.2f} INCHES.")
    print(f"THE MONTH OF {months_of_year[month_lowest]} HAD THE LOWEST RAINFALL OF {lowest_rainfall:.2f} INCHES.")

# Call main
main()

