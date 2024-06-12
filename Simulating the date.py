#Name:Nana Kwasi Owusu
#Date: 23 April 2024
#Program Description: This program represents dates in a calendar date format

#this module takes the intInRange function from inputroutines file. These functions are used to make sure the user inputs the right values
from inputroutines import intInRange

#this module takes the Date class from the the date file. The methods in this class are used to display the date in calendar date format
from date import Date

#this function makes sure that the day that the user inputs falls within the possible number of days for that month
def dayValidation(month):
    maxDaysForMonth = {
        1:31, 2:28, 3:31,
        4:30, 5:31, 6:30,
        7:31, 8:31, 9:30,
        10:31, 11:30, 12:31
        }
    while True:
        try:
            day = int(input('Enter the day (must be an integer value between 1 and 31 depending on the month): '))
            if not 1 <= day <= maxDaysForMonth.get(month,0):
                raise ValueError("Invalid day value")
            break
        except ValueError as e:
            print(e)
            day = int(input('Enter the day (must be an integer value between 1 and 31 depending on the month): '))
    return day

if __name__ == "__main__":
    #this part of the program takes input from the user and makes sure they are within the assigned ranges 
    print("Enter the month (must be an integer value between 1 and 12): ",end='')
    Month1 = intInRange(1,12)
    Day1 = dayValidation(Month1)
    print("Enter the year (must be a four-digit  positive integer): ",end='')
    Year1 = intInRange(1000,9999)
    
    #this part of the program takes input from the user and makes sure they are within the assigned ranges 
    print("\nNow you are going to input results for another date")
    print("Enter the month (must be an integer value between 1 and 12): ",end='')
    Month2 = intInRange(1,12)
    Day2 = dayValidation(Month2)
    print("Enter the year (must be a four-digit  positive integer): ",end='')
    Year2 = intInRange(1000,9999)
    
    #First date object
    Date1 = Date(Month1,Day1,Year1)
    
    #Second date object
    Date2 = Date(Month2,Day2,Year2)
    
    #These tests are used to test the getter methods
    print(f"\nThe first date inputted by the user is: {Date1}")
    print(f"The first month inputted by the user is: {Date1.getMonth()}")
    print(f"The first day inputted by the user is: {Date1.getDay()}")
    print(f"The first year inputted by the user is: {Date1.getYear()}")
    
    print(f"\nThe second date inputted by the user is: {Date2}")
    print(f"The second month inputted by the user is: {Date2.getMonth()}")
    print(f"The second day inputted by the user is: {Date2.getDay()}")
    print(f"The second year inputted by the user is: {Date2.getYear()}")
    
    
    #These tests are used to test the overloaded operators
    print(f'\nDate 1 == Date 2: {Date1 == Date2}')
    print(f'Date 1 != Date 2: {Date1 != Date2}')
    print(f'Date 1 < Date 2: {Date1 < Date2}')
    print(f'Date 1 <= Date 2: {Date1 <= Date2}')
    print(f'Date 1 > Date 2: {Date1 > Date2}')
    print(f'Date 1 >= Date 2: {Date1 >= Date2}')
    
    #These tests are used to test the subscript operator
    print(f'\nThe month for Date 1 is: {Date1[0]}')
    print(f'The day for Date 1 is: {Date1[1]}')
    print(f'The year for Date 1 is: {Date1[2]}')
    print(f'The month for Date 2 is: {Date2[0]}')
    print(f'The day for Date 2 is: {Date2[1]}')
    print(f'The year for Date 2 is: {Date2[2]}')
    try:
        print(f"Date1[5]: {Date1[5]}")
    except IndexError as e:
        print(e)
    
    #This statement asks the user for the number of days to add to the dates they inputted
    daysToAdd = int(input('\nEnter a number of days to add to date 1 and date 2 for testing: '))

    #This test is used to test the setter methods
    Date1.changeDate(daysToAdd)
    print(f'New Date 1 after adding {daysToAdd}: {Date1}')
    Date2.changeDate(daysToAdd)
    print(f'New Date 2 after adding {daysToAdd}: {Date2}')
        
