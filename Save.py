import json
import  numpy as np

DATA_FILE_JSON = "data.json"

#After a wide search i found that store data and save it to a binary file in NumPy
#is more efficient and faster than storing using json 

def is_exist_json(elemnt):
    #Check if Given value exist in the json file
    with open(DATA_FILE_JSON, "r+") as file:
        file_dict = json.load(file)
        if str(elemnt) in file_dict:
            return file_dict.get(str(elemnt)) 
        else:
            #Key not exist
            return -1 
        
def save_toFile_json(elemnt,result):
    #This function save The results, if given number is perfect or not
    temp_dict = {}
    temp_dict[elemnt]=result
    print(temp_dict) 
    
    with open(DATA_FILE_JSON, "r+") as file:
        file_dict = json.load(file)
        file_dict.update(temp_dict)
        file.seek(0)
        json.dump(file_dict, file)
 
