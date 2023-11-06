list1 = [2,4,8,10,12,14,16,18] #enclosed in square brackets mutable ordered collection of items
print(list1, type(list1))
print('\n')

tuple1 = ('a', "b" , "c") #ordered collection of immutable objects but can be changed by converting into list
tuple2 = (1,) #if comma not placed the type function will return integer
print(tuple1,type(tuple1),"\n",tuple2,type(tuple2))
print("\n")

tup = (15, [15,12,"python"])
print(type(tup))
print(tup[1][-1])
tup[1][-1] = "python programming"
print(tup)
print('\n')

print(chr(35646)) #get an ascii character
print(ord("😂")) #get the ascii value of a character


set1 = {} #empty braces will print dictionary type 
print(type(set1))

set1 = set() #empty set
print(type(set1)) #sets cannot be duplicates because they are hashed key 

dict1={} #create an empty dictionary
dict1 = {1:"python", 2:"java", "program":"Script"}
print(dict1)

#difference between none empty a position is holding none {no values} or may be empty