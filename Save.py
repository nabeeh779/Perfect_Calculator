import json
from logging import exception
import  numpy as np

DATA_FILE_NUMPY = "data.npy"
DATA_FILE_JSON = "data.json"

#After a wide search i found that store data and save it to a binary file in NumPy
#is more efficient and faster than storing using json 

def extarct_perfect_range(start,end):
    #Return perfect numbers in given range
    load_dict = np.load(DATA_FILE_NUMPY,allow_pickle=True)
    temp = []
    for dict in load_dict:
        key_list = list(dict.keys())
        val_list = list(dict.values())
        try:  
            position = val_list.index(True)
            if int(end)>key_list[position] > int(start) :
                temp.append(key_list[position])
        except ValueError:
            None
    return temp
def extract_allPerfect_numbers():
    #This function return all perfect numbers in list
    #And return the count of all perfect numbers in it
    load_dict = np.load(DATA_FILE_NUMPY,allow_pickle=True)
    counter = 0
    temp = []
    for dict in load_dict:
        key_list = list(dict.keys())
        val_list = list(dict.values())
        
        try:  
            position = val_list.index(True)
            temp.append(key_list[position])
            counter += 1
        except ValueError:
            None
    return temp,counter

#extract_allPerfect_numbers()
def save_toFile_numpy(elemnt,result):
    #This function save The results, if given number is perfect or not
    temp_dict = {}
    temp_dict[elemnt]=result
    load_dict = np.load(DATA_FILE_NUMPY,allow_pickle=True)
    load_dict = np.append(load_dict, temp_dict)
    np.save(DATA_FILE_NUMPY,load_dict)
    
def is_exist_numpy(elemnt):
    #Check if Given value exist in the npy file
    load_dict = np.load(DATA_FILE_NUMPY,allow_pickle=True)
    for dict in load_dict:
        if elemnt in dict:
          return dict.get(elemnt) 
        
    #Key not exist
    return -1 

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
 
