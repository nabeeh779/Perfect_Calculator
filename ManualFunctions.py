#In This File We Can Add Any Function We Need 
#TO USE IN DIFFRENT PLACES
#
from difflib import restore
import re
from unittest import result

from numpy import save
import Save

def split_numbers(var):
    #This function help split two given numbers splitted by '-'
    #and return it in a list
    return var.split('-')

def choose_function(var):
    print(var)
    if '-' in var:
        #Third option in API
        lista = split_numbers(var)
        print(lista)
        return Save.extarct_perfect_range(lista[0],lista[1])
    if var == 'X':#second option in API      
        return Save.extract_allPerfect_numbers()
    
    if isinstance(int(var),int):
        #first option
        print(f"OP1 - {var}")
        result = Save.is_exist_numpy(int(var),0)
        print(result)
        if result == -1:
            result = False
        return result,check_if_perfect(int(var))
    

        
def get_input():
    #Gets the input from user
    return input("Enter a number to check:")

def check_if_perfect(n): 
    #This function check if number is perfect
    #First we check if the number exist in the DB if not we add it 
    result = Save.is_exist_numpy(n,1)
    if result == -1:
        #Check If the new number is perfect and save the result 
        sum = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                sum = sum + i + n/i
            i += 1
        if sum == n and n!=1:
            Save.save_toFile_numpy(n,True)
            return True
        else:
            Save.save_toFile_numpy(n,False)
            return False       
    else:
        return result