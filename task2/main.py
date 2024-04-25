def get_cats_info(path:str)->list:
    """
    Function returns information about cats from the data file as list of dictionaries.
    Input parameter: path to the file
    Output: list of dictionaries
    """
    try:
        with open(path,'r',encoding='utf-8') as fn: #opening the file for reading and setting the encoding to utf-8
             
             cats_info_list=list() #creating empty list

             for el in fn.readlines(): #reading line from the file
                key,name,age=el.strip().split(",") # parsing line into 3 values
                cats_info_list.append({"id":key,"name":name,"age":age}) #creating dictionary and appending it to the list

        return cats_info_list

    except FileNotFoundError:
        print("The file  was not found!")