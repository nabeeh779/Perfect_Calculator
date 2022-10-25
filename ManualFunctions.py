#In This File We Can Add Any Function We Need
#
#
from difflib import restore
import re
from unittest import result
import Save

def get_input():
    #Gets the input from user
    return input("Enter a number to check:")

def check_if_perfect(n): 
    #This function check if number is perfect
    #First we check if the number exist in the DB if not we add it 
    result = Save.is_exist(n)
    if result == -1:
        #Check If the new number is perfect and save the result 
        sum = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                sum = sum + i + n/i
            i += 1
        if sum == n and n!=1:
            Save.save_toFile(n,True)
            return True
        else:
            Save.save_toFile(n,False)
            return False       
    else:
        return result