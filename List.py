



list=["Python","Data Science","Data Analytics","Panda","Numpy"]
print(list)
#adding element in list
list.append("Seaborn")
print(list)

list2=["java","Spring","Springboot"]
#combination of lists using extends function
combination_oflist=list.extend(list2)

print(combination_oflist)

list.insert(2,"Matplotlib")

print(list)

print(list+list2)


#take input from the user for the size of the list
list1= []
# number of elements as input
n=int(input("Enter the length of the list : "))

# iterating till the range
for i in range (0,n):
    num=int(input(f"Enter the {i} index  number of the list"))
    # adding the element
    list1.append(num)
print(list1)


#sorting of lists
list3=[5,8,96,12,45,20,78,23,65,32]
list3.sort()
print(list3)

list4=["React","JavaScript","Django","Html","Css","Java"]
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

# we cannot sort list when there is multiple data type in the same list
# list=["React",1,"JavaScript",4]

# sorting using sorted function

list5=[5,8,96,12,45,20,78,23,65,32]
sorted_list=sorted(list5)
print(sorted_list)
print(len(list5))
# the difference between sort() and shorted() is that the sorted function ceate the new list while sort function modified the existing list

print(max(list5))
print(min(list5))

list5.clear() # it delete the list elements but list exist with no elements
print(list5)


# usijng = to copy the lists


list5=[5,8,96,12,45,20,78,23,65,32]   
print("Before modification list5", list5)
list6=list5
print("before modification list6", list6)


list6[2]=100
print("After modification list6", list6)
print("After modification list 5", list5)

# using = operator to copy list to another then it only represent the same memory location any modification affects both list
# to avoid this we use concept of shallow copying

list5=[5,8,96,12,45,20,78,23,65,32]
list7=list5.copy()
print("Before modification list5", list5)
print("Before modification list7", list7)

list7[2]=500

print("After modification list7", list7)
print("After modification list5", list5) # here there is no affect in list 5


# concept of shallow coppy is not working for the nested list 
# If we want to work on nested list we cannot use shallow copy because it acts like an copy it store in same memory location
list8=[[4,23,6,9],[12,96,15,6]]
list9=list8.copy()

print("Before modification list8", list8)

list9[0][1]=1000

print("After modification list9", list9)

print("After modification list8", list8) # here there is no affect in list 8
print(id(list8))
print(id(list9))
if id(list8[0])==id(list9[0]):
    print("Both list9 and list8 are same memory location")
else:
    print("Both list9 and list8 are not same memory location")
# for nested list we can use deepcopy function from copy module

import copy

list8=[[4,23,6,9],[12,96,15,6]]
list10=copy.deepcopy(list8)
print("Before modification list10", list10)
list10[0][1]=1000
print("After modification list10", list10)
print("After modification list8", list8) # here there is no affect in list 8
print(id(list8))
print(id(list10))

if id(list8[0])==id(list10[0]):
    print("Both list10 and list8 are same memory location")
else:
    print("Both list10 and list8 are not same memory location")
    
    # here every object in list they are refrencing to different memory location
    
# count the number of occurences of an element in list
products=["Diary","Bakery","Grocery","Bakery","Diary","Cosmetic"]
print(products.count("Bakery"))

number=[9,8,3,2,2,3,8,5,8,9,8]
print(number.count(8))

# find the index of an element in list it return the lowest position in case of multiple occurence

print(products.index("Diary"))

number=[9,8,3,2,2,3,8,5,8,9,8]

print(number.index(8))

# remove elements from a list

products.remove("Diary")
print(products)

number=[9,8,3,2,2,3,8,5,8,9,8]

number.remove(8)
print(number)

#using pop

print(products.pop()) # it remove the last element

print(products)

print(number.pop(2)) # remove specific elements
print(number) 

# slice a list 

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[1:5]) # it print 2,3,4,5

print(numbers[:5]) # it print 1,2,3,4,5

print(numbers[5:]) # it print 6,7,8,9,10

print(numbers[::2]) # it print 1,3,5,7,9 here 2 represent the increment value

print(numbers[::-1]) # it print 10,9,8,7,6,5,4,3,2,1 in reverse order


