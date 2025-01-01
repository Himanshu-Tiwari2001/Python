dict1={
    "Name": "Rohit",
    "roll":21,
    "Marks": 85,
    "Grade": "A"
}


y=dict1.get("roll")
print(y)
print(type(dict1))

for i in dict1:
    print(i,dict1[i])
    
print(len(dict1))    

dict1["city"]="Delhi"
print((dict1))
dict2={
    "name":"Mohit",
    "roll":22,
    "Marks": 90,
    "Grade": "B"
    
}
dict1.update(dict2)
print(dict1)
# for i in dict1:
#     print(i,dict1[i])
     
# dict1.pop("name")
# for i in dict1:
#     print(i,dict1[i])

dict3={
     "detail1":{
         "Name":"Rohit",
         "roll":21,
         "Marks": 85,
         "Grade": "A"
     },
     "detail2":{
         "Name":"Mohit",
         "roll":22,
         "Marks": 90,
         "Grade": "B"
         
     },
     
}
print(dict3["detail1"]["Name"])
print("the roll no of details2 is",dict3["detail2"]["roll"])

# Dictionary word count example

from collections import Counter
sentence="I love programming and Python programming is very easy"
words=sentence.split()
word_count=Counter(words)
print(word_count)

# count the word and store the frequency in the form of dictionary
sentence ="canyou can as a canner can can a can" # any random sentence containing reptitive words
word_count={}

for word in sentence.split():
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1 # this line is important because adding +1 to word count without initializing then the  code throws an error because the key is not initialized and we are trying to add 1 to an the uninitialized key’s value

print("The dictionary will be")
print(word_count)  

# using the concept of DEFAULT DICTIONARY in orde
# import the defaultdict from collection module
print("----------------------------------------------")
from collections import defaultdict
sentence1="canyou can as a canner can can a canner can" # any random sentence containing

word_count=defaultdict(int)

for word in sentence1.split():
        word_count[word]+=1
# print(word_count) 

for key,value in word_count.items():
    print(key,value)
 
 
# length of the dictionary

print("----------------------------------------------")
print("Length of the dictionary is",len(word_count))

# deleting a key from dictionary

print("----------------------------------------------")
del word_count["canyou"]
print(word_count)

# removing all the elements from dictionary

print("----------------------------------------------")
# word_count.clear()
# print(word_count)

# checking if a key is present in dictionary

print("----------------------------------------------")
print("canyou" in word_count)
print("can" in word_count)

# converting dictionary in to printable string representation
print("----------------------------------------------")
item_purchased={"Sanatizer":2,"glass":3,"brush":2}

print(str(item_purchased))
type(item_purchased)

# dictionary operations

print("----------------------------------------------")
# create a shallow copy
items={"sanatizer":2,"glass":3,"brush":5}
itemscopy=items.copy()
print(itemscopy)

print(items.keys())#return list of keys in dictionary
print(items.values())#it return the list of values in dictionary
print(items.items())#it returns list of tuples where each tuple contains key and value

#retrieve the number of sanatizer is purchased
print(items.get("sanatizer")) #output 2

# if there is no key in the dictionary ,thus get() function return none

print(items.get("pen")) #output None

# adding new key-value pair

items["pen"]=10
print(items)

# updating the value of a key

items["pen"]=15
print(items)

# removing a key-value pair

items.pop("pen")
print(items)

# merging two dictionaries

dict1={"name":"Rohit","age":21}
dict2={"city":"Delhi","grade":"A"}

dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

#set default key if it is not present in existing dictionary

dict4={"name":"Rohit","age":21}
dict4.setdefault("city","Delhi")
print(dict4)

# deleting a key from dictionary

del dict4["age"]
print(dict4)

# create a dictionary from tuple
tuple=("ord_id","cust_id","amount")
# type cast the tuple to dict using fromkey() function
# all element are converted in to key
# value for each key will be none 
new_dict=dict.fromkeys(tuple)
print("dictionay:",new_dict)

# assign defaut value to dictionary

new_dict=dict.fromkeys(tuple,2)
print("dictionay:",new_dict)




#######################################################################
# create a list of items name as key 
# create a list of selling price as values

items=["pen","pencil","eraser"]
prices=[10,5,2]

# create a dictionary from two lists
# use zip() function to creat dictionary
# here zip () pairs the corresponding elements of the list as a key and value of dictionary

item_dict=dict(zip(items,prices))
print(item_dict)

#  Did You Know? A tuple is immutable. However, if the tuple contains a list or a dictionary inside it, then the list or the dictionary that is contained within the tuple can be modified.
