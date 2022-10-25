import json

DATA_FILE = "data.json"


def is_exist(num):
    #Check if Given value exist in the json file
    with open(DATA_FILE, "r+") as file:
        file_dict = json.load(file)
        if str(num) in file_dict:
            return file_dict.get(str(num)) 
        else:
            #Key not exist
            return -1 
        
def save_toFile(number,isPerfect):
    #This function save The results, if given number is perfect or not
    temp_dict = {}
    temp_dict[number]=isPerfect
    print(temp_dict) 
    
    with open(DATA_FILE, "r+") as file:
        file_dict = json.load(file)
        file_dict.update(temp_dict)
        file.seek(0)
        json.dump(file_dict, file)
 
