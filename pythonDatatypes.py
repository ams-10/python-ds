"""numerical int float complex"""
"""sequence type {ordered list,tuple,string} unordered {set,dictionary}"""
"""boolean true false"""
#float precision == 50  
#print commented part 
def fun():
    """IT LORDS"""
    return print(fun.__doc__)

#iskeyword() => the function is used to check if its key word or not 

"""string datatypes""" 
string1 = "Python" #a string is a sequence of characters it is immutable
print(string1) #can print multiple by using * ex *5
# string1[3] = "h" #string does not have assignments

import keyword
string =  "python programming"
print(string[0:4:-1]) #string slicing [start:end:step]
print(keyword.iskeyword(string)) 
