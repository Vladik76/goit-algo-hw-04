def total_salary(path:str)->tuple[float,float]:
    """
    Function calculates total salary and average salary from the data from file.
    Input parameter: path to the file
    Output: tuple in format (total,average)
    """
    try:
        with open(path,'r',encoding='utf-8') as fn: #opening the file for reading and setting the encoding to utf-8
            salaries=[float(el.split(',')[1].strip()) for el in fn.readlines()] #reading file to the list of salaries. Convert each value to float
            
            salaries_total=sum(salaries) # calculating the sum of the salaries
            salary_average=round(salaries_total / len(salaries),2)  # calculating average salary from the list of the salaries

            return (salaries_total,salary_average) # returning tuple

    except FileNotFoundError:
        print("The file with the salaries was not found!")