# File Name:   date.py
# Purpose:     Class to represent a date in calendar time.
# Known facts: month is an integer value between 1 and 12
#              day is an integer value between 1 and 31
#              year is a four-digit non-negative number

# Author:      Nana Kwasi Owusu
# Date:        April 23, 2024

class Date:
    #constructor with default values for each parameter
    def __init__(self, month=1, day=1, year=1900):
        self.__month = month
        self.__day = day
        self.__year = year
        
    #getters
    def getMonth(self):
        return self.__month
    
    def getDay(self):
        return self.__day
    
    def getYear(self):
        return self.__year
    
    #setters
    def changeDate(self,dayToAdd):
        maxDaysForMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.__day += dayToAdd
        while self.__day > maxDaysForMonth[self.__month - 1]:
            self.__day -= maxDaysForMonth[self.__month - 1]
            self.__month +=1
            if self.__month > 12:
                self.__month = 1
                self.__year += 1
    
    #Operator overloading methods
    def __getitem__(self,index):
        if index ==0:
            return self.__month
        elif index ==1:
            return self.__day
        elif index == 2:
            return self.__year
        else:
            raise IndexError('Index out of bounds')
        
    def __str__(self):
        date = f"{self.__month:02d}/{self.__day:02d}/{self.__year}"
        return date
    
    
    def __eq__(self,other):
        if self[0] != other[0]:
            return False
        return (self[1]==other[1]) and (self[2]==other[2])
    
    
    def __ne__(self,other):
        return not(self==other)
    
    
    def __lt__(self,other):
        if self[2] < other[2]:
            return True
        elif self[2] == other[2]:
                if self[1] < other [1]:
                    return True
                elif self[1] == other[1]:
                    if self[0] < other[0]:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
                
                
    def __le__(self,other):
        return (self < other) or (self==other)
                
                
    def __gt__(self,other):
        return other < self
                
                
    def __ge__(self,other):
        return(self > other) or (self==other)
    
    
    
        
        