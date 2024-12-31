# Syntax
# lambda arguments:expression
# in python lambda function is also called anonymous function that can be defined in a single line of code without a name. it is useful when need a simple function the we don't want to 9define explicitely using the def keyword. 




f=lambda x,y:x+y
print(type(f))
print(f(2,3))

# Lambda function can take any number of arguments but only one expression.
# write a lambda fuction which can square the each elemnt in the list

numbers=[1,2,3,4,5]
squares=list(map(lambda x:x**2,numbers))
print(squares)

number=[5,6,7,8,9,12,14]
sqaure_ofnum= list(map(lambda x:x**2,number))
print(sqaure_ofnum)

# write a lambda function which can filter the even numbers from the list

numbers=[1,2,3,4,5,6,7,8,9]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

# write a lamda function which can return the length of the string
string = lambda x:len(x) 
print(string('Hello World')) # Output: 11

# write a lambda function which can return the sum of the elements in a list

numbers=[1,2,3,4,5]
sum_of_numbers=lambda x:sum(x)
print(sum_of_numbers(numbers)) # Output: 15


number=[5,4,3,2,1]
sumof_num = (lambda x:sum(x))
print(sumof_num(number)) # Output: 15


# write a lambda function which can return the maximum element in a list
number1=[5,4,3,2,1,10,7,12]
maxof_num=lambda x:max(x)
print(maxof_num(number1)) # Output: 12

# write a lambda function which can return the minimum element in a list
number [5,4,9,15,2,1]
minof_num=lambda x:min(x)
print(minof_num(number)) # Output: 1

# write a lambda function which can return the average of the elements in a list

numbers=[5,4,3,2,1,10,7,12]
average_of_numbers=lambda x:sum(x)/len(x)
print(average_of_numbers(numbers)) # Output: 7.071428571428571

# write a lambda function which can return the product of the elements in a list
numbers=[5,4,3,2,1,10,7,12]

product_of_numbers=lambda x:1 if len(x)==0 else x[0]*product_of_numbers(x[1:])

print(product_of_numbers(numbers)) # Output: 172800 

# write a lambda function which can return the factorial of a number

factorial=lambda x:1 if x==0 else x*factorial(x-1)
print(factorial(5)) # Output: 120

# write a lambda function which can return the fibonacci sequence till the nth number

fibonacci=lambda n:1 if n<=1 else fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10)) # Output: 55

# write a lambda function which can return the sum of squares of the first n natural numbers

sum_of_squares=lambda n:n*(n+1)*(2*n+1)//6
print(sum_of_squares(10)) # Output: 385

# write a lambda function which can return the sum of cubes of the first n natural numbers

sum_of_cubes=lambda n:n*(n+1)//2*(2*n+1)*(2*n+1)//3
print(sum_of_cubes(10)) # Output: 2250

# write a lambda function which can return the sum of the first n prime numbers

is_prime=lambda num: all(num%i!=0 for i in range(2,int(num**0.5)+1))
sum_of_primes=lambda n: sum(i for i in range(2,n+1) if is_prime(i))
print(sum_of_primes(10)) # Output: 17

# write a lambda function which can return the sum of the first n Fibonacci numbers

fibonacci=lambda n:1 if n<=1 else fibonacci(n-1)+fibonacci(n-2)
sum_of_fibonacci=lambda n: sum(fibonacci(i) for i in range(n))
print(sum_of_fibonacci(10)) # Output: 44

# write a lambda function which can return the sum of the first n Lucas numbers

lucas=lambda n:2 if n<=1 else lucas(n-1)+lucas(n-2)
sum_of_lucas=lambda n: sum(lucas(i) for i in range(n))
print(sum_of_lucas(10)) # Output: 123

# write a lambda function which can return the sum of the first n numbers in the Fibonacci sequence

fibonacci=lambda n:1 if n<=1 else fibonacci(n-1)+fibonacci(n-2)
sum_of_numbers=lambda n: sum(fibonacci(i) for i in range(n))
print(sum_of_numbers(10)) # Output: 44

# write a lambda function which can return the sum of the first n numbers in the Lucas sequence

lucas=lambda n:2 if n<=1 else lucas(n-1)+lucas(n-2)
sum_of_numbers=lambda n: sum(lucas(i) for i in range(n))
print(sum_of_numbers(10)) # Output: 123

# write a lambda function which can return the sum of the first n numbers in the Pell sequence

pell=lambda n:2 if n<=1 else 2*pell(n-1)+pell(n-2)
sum_of_numbers=lambda n: sum(pell(i) for i in range(n))
print(sum_of_numbers(10)) # Output: 143

# write a lambda function which can return the sum of the first n numbers in the Tribonacci sequence

tribonacci=lambda n:1 if n<=2 else tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
sum_of_numbers=lambda n: sum(tribonacci(i) for i in range(n))
print(sum_of_numbers(10)) # Output: 45

# write a lambda function which can return the sum of the first n numbers in the Catalan sequence       

catalan=lambda n:1 if n<=1 else (2*(2*n-1)*catalan(n-1))//(n+1)
sum_of_numbers=lambda n: sum(catalan(i) for i in range(n))
print(sum_of_numbers(10)) # Output: 429

# write a lambda function which sort the list of string based on their length:

strings=['apple','banana','cherry','date','elderberry']
sorted_strings=lambda x: sorted(x, key=len)
print(sorted_strings(strings)) # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# write a lambda function which sort the list of string based on their length in descending order:

strings=['apple','banana','cherry','date','elderberry']
sorted_strings=lambda x: sorted(x, key=len, reverse=True)
print(sorted_strings(strings)) # Output: ['elderberry', 'date', 'cherry', 'banana', 'apple']

# write a lambda function which sort the list of dictionary based on specific key:

data=[{'name':'John','age':25},{'name':'Alice','age':30},{'name':'Bob','age':28}]
sorted_data=lambda x: sorted(x, key=lambda i: i['age'])
print(sorted_data(data)) # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 28}, {'name': 'John', 'age': 25}]

# write a lambda function which sort the list of dictionary based on specific key in descending order:

data=[{'name':'John','age':25},{'name':'Alice','age':30},{'name':'Bob','age':28}]
sorted_data=lambda x: sorted(x, key=lambda i: i['age'], reverse=True)
print(sorted_data(data)) # Output: [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 28}]
# finding the max value in a dictionary

max_value=lambda x: max(x, key=lambda i: i['age'])
print(max_value(data)) # Output: {'name': 'John', 'age': 25}

# finding the min value in a dictionary

min_value=lambda x: min(x, key=lambda i: i['age'])
print(min_value(data)) # Output: {'name': 'Alice', 'age': 30}

# finding the sum of all values in a dictionary

data = {"a":10, "b":20, "c":30, "d":40, "e":60}
sum_values=lambda x: sum(data.values())
print(sum_values(data)) # Output: 180

# finding the product of all values in a dictionary
from functools import reduce
data = {"a":10, "b":20, "c":30, "d":40, "e":60}
product_values=lambda x: reduce(lambda a, b: a*b, data.values())
print(product_values(data)) # Output: 12000000000000000

# finding the average of all values in a dictionary

data = {"a":10, "b":20, "c":30, "d":40, "e":60}
average_values=lambda x: sum(data.values())/len(data)
print(average_values(data)) # Output: 24.0

# finding the median of all values in a dictionary 


from statistics import median
data = {"a":10, "b":20, "c":30, "d":40, "e":60}
median_values=lambda x: median(data.values())
print(median_values(data)) # Output: 30.0

# finding the mode of all values in a dictionary

from collections import Counter
data = {"a":10, "b":20, "c":30, "d":40, "e":60}
mode_values=lambda x: Counter(data.values()).most_common(1)[0][0]
print(mode_values(data)) # Output: 20


#grouping of a list of strings based on their first character
from itertools import groupby
strings=['apple','banana','cherry','date','elderberry']
grouped_strings=lambda x: {k: list(v) for k, v in groupby(x, key=lambda i: i[0])}
print(grouped_strings(strings)) # Output: {'a': ['apple'], 'b': ['banana'], 'c': ['cherry'], 'd': ['date'], 'e': ['elderberry']}

# grouping of a list of strings based on their first character in descending order

from itertools import groupby
strings=['apple','banana','cherry','date','elderberry']
grouped_strings=lambda x: {k: list(v) for k, v in sorted(groupby(x, key=lambda i: i[0]), reverse=True)}
print(grouped_strings(strings)) # Output: {'e': ['elderberry'], 'd': ['date'], 'c': ['cherry'], 'b': ['banana'], 'a': ['apple']}

# finding the longest string in a list

strings=['apple','banana','cherry','date','elderberry']
longest_string=lambda x: max(x, key=len)
print(longest_string(strings)) # Output: elderberry

# finding the shortest string in a list

strings=['apple','banana','cherry','date','elderberry']
shortest_string=lambda x: min(x, key=len)
print(shortest_string(strings)) # Output: apple

# finding the most frequent string in a list

from collections import Counter
strings=['apple','banana','cherry','date','elderberry','apple','banana']
most_frequent_string=lambda x: Counter(x).most_common(1)[0][0]
print(most_frequent_string(strings)) # Output: apple

# finding the least frequent string in a list

from collections import Counter
strings=['apple','banana','cherry','date','elderberry','apple','banana']
least_frequent_string=lambda x: Counter(x).most_common()[-1][0]
print(least_frequent_string(strings)) # Output: cherry
















