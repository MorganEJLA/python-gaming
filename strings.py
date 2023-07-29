#data type used to communicate with the user. Need some communication with the player/user

#strings

# '' or " "

#Accessing elements of a string
#Forward direction indexing

# 0 1 2 3 4 5 
# P Y T H O N

# -6 -5 -4 -3 -2 -1
#backward direction indexing


# s = "CUPCAKE"
# print(s[3])

#Strings Methods

#Why have string methods?
#Manipulate strings etc 


print("lollipop".capitalize())
#Lollipop
print("Brazil".lower())
#brazil
print("brazil".upper())
#BRAZIL



#join the strings
print("----------------------------------------")
info = ("I", "am", "Steve")
print(" ".join(info))
info = "I am Steve"
print(info.split())


print("apples, peaches, banana, pear, pear".count('a'))

#index string method

# print("HELLO".index('E'))

# country = "Azores"
# year = "2024"

# print(f'I am going to the {country} in {year}')

destination = input("enter your destination for 2024")
print(f'You are going to {destination}!')