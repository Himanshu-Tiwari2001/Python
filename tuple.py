tuple1=(1,2,8,7,41,65,32,23,"a","b","c","d","e","f")
print (tuple1)
print(type(tuple1))

#Sorting the tuple elements using the sorted() function in acending order
number=(1,2,8,7,41,65,32,23)
sorted_tuple=sorted(number)
print(sorted_tuple)
# in descending order

sorted_tuple_descending=sorted(number,reverse=True)
print(sorted_tuple_descending)
#Reversing the sorted tuple

reversed_tuple=sorted_tuple[::-1]
print(reversed_tuple)
print(type(reversed_tuple)) # <class"List">
# note->>>>> List has a sort() function but a tuple does not have a sort() function. However, you can use the sorted() function to sort both a list & a tuple.
# The sorted() returns a list even if you pass a tuple to it.

# repating the tuple element
order_recieved=("Pizza","Cola")

# Creating a new tuple by repeating the existing tuple

repeated_tuple=order_recieved*3 # here it repeats the exixting tuple 3 times
print(repeated_tuple)

# concatenating two tuple 
order_online=("burger","pizza","Ice cream")
order_offline=("Fruit","Noodle")
total_order=order_online+order_offline
print("after concatenating \n",total_order)

# Checking existence of an element using membership operators

print("Pizza" in order_online) # True
print("Fruit" in total_order) # True
print("Ice cream" in order_online) # False

# iterating over the elements in tuple
print("The elements in tuple" )
for item in total_order:
    print(item)
    
# Counting the number of elements in the tuple

print("Number of elements in the tuple is ",len(total_order)) # 5





# getting min or max values from tuples

print("Min value from tuple is ",min(order_online)) # Burger
print("Max value from tuple is ",max(order_online)) # Pizza

# note since the tuple is immutable ,a new element cnnot be modified
price=(100,200,250,350,450)
# del price[0]

 
# we can convert the tuple to a list and then modify it and then convert it back to a tuple
price1=(100,200,250,350,450)
price_list=list(price1)
price_list[0]=150
price1=tuple(price_list)

print("Modified price tuple is ",price1)

# converting tuple to dictionary
purchase_item=("Sanatizer","Chocolate","Biscuit","Brush")

purchase_price=("20","30","15","10")

# to do that we have to use zip() function in python it combine two tuple it takes the two tuple as  parameter/Argumnent and return dictionary having key and value
purchase_dict=dict(zip(purchase_item,purchase_price))
print("The converted tuple",purchase_dict)

#Did You Know? Because tuple is immutable, a tuple needs lesser memory than lists.
#Did You Know? Lesser memory fragmentation is better in terms of performance. Python can reuse a tuple which results in reduction of memory fragmentation and can speed up memory allocations. If a tuple is no longer required and has less than 20 elements, instead of deleting it permanently, Python reserves it temporarily.
