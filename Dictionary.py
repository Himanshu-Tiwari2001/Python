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