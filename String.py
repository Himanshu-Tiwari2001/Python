text ="I love cricket"
print(text)

# Changing the case of text
print("upper case->"+text.upper() +  " \nLower case-> "+text.lower())

# split the text

print("Splitting text -> "+str(text.split()))  #output : Splitting text -> ['I', 'love', 'Cricket']

print(text[:]) # output : I love Cricket
print(text[0:6]) # output : I Love

print(text[0:10]) # output : I love Cri
print(text[7:]) # output :Cricket

# count the number of characters in the text

print("Length of the text -> ",len(text)) # output : Length of the text -> 14

#negative indexing
print(text[-7:-1])
 
 # reverse the string using negative indexing
print(text[::-1]) # output :
# reverse the string and display the last third character
print(text[::-1][-3])

# replace a character in the string
text2=text.replace("cricket","badminton")
print(text2)

print(text.title() )

# concept of seperatorin string
date="31","12","2024"
seperator="-"
seperator.join(date)

print(seperator.join(date)) # output : 31-12-2024

# use of strip function

text3="   hello world   "
print(text3.strip()) # output : hello world

text3="hello world****"

print(text3.strip("*")) # output : hello world

text3="*****hello world" # output : hello world
print(text3.strip("*"))
# use of split function

print(text.split(" ")) # output : ['I', 'love', 'cricket']
print(text.split())