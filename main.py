
'''
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

'''

# print("Twink, twinkle, little star,\n   How i wonder what you are!\n       Up above the world so high,\n       Like a diamond in the sky.\nTwinkle, twinkle little star,\n    How i wonder what you are")

'''
2. Write a Python program to get the Python version you are using. Go to the editor
Click me to see the sample solution

'''
# import sys
# print(sys.version)

'''
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
Click me to see the sample solution

'''

'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504

'''

# from math import pi

# uinp = float(input("Please type the radius of a circle: "))

# diameter = pi * uinp ** 2
# print(diameter)


'''
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor
Click me to see the sample solution

'''

# first_name = input("Please type your first name: ")
# last_name = input("Please type your last name: ")

# print(f"Hello {last_name} {first_name}. How are you today?")

'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
Click me to see the sample solution


'''

# mylist = [


# ]

# uinp = input("Please type a series of numbers: ")

# values = uinp.split(",")

# mylist.append(values)
# mytuple = tuple(values)


# print(mylist)
# print(mytuple)

'''
8. Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
Click me to see the sample solution

'''
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[-1])


'''
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

'''

# exam_st_date = (11, 12, 2014)

# print("The exam wil start from: %i / %i / %i" %exam_st_date)

'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615

'''

# n = int(input("Please type a number: "))


# a1 = int("%i" % n )
# a2 = int("%i%i" % (n, n))
# a3 = int("%i%i%i" % (n, n, n))
# print(a1+a2+a3)

'''11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

# print(abs.__doc__)

'''
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
Click me to see the sample solution

'''

# import calendar

# y = int(input("Please type the year: "))
# m = int(input("Please type the month: "))

# print(calendar.month(y, m))

'''
13. Write a Python program to print the following here document. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

'''
# print(
# """
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """
# )

'''
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

'''

# from datetime import date

# date1 = date(2020, 12, 8)
# date2 = date(2020, 12, 21)
# date3 = date2 - date1
# print(date3.days)

'''
15. Write a Python program to get the volume of a sphere with radius 6.

'''

# from math import pi

# uinp = float(input("Please type the radius of the circle: "))

# v = 4/3*pi* uinp**3

# print(f"The volume of the sphere is {v}")

'''
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

'''


# def difference(num):
#     if num < 17:
#         return num - 17
#     else:
#         return (num - 17) * 2

# print(difference(25))
# print(difference(10)),

'''
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

'''



# def difference(a, b, c):
#     sum = a + b + c
#     if a == b == c:
#         sum = sum * 3
#     return sum
   
        
# print(difference(1, 2, 3))
# print(difference(4, 4, 4))

'''
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

'''

# a = input("Please type some words: ")

# if a.startswith("Is"):
#     print(a)
# else:
#     print(f"Is {a}")

'''
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string

'''

inp = input("Please type a number: ")

while True:
    inp = input("Please type a number: ")
    if not inp.isdigit():
        print("please type a valid number:") 
        break
    elif inp < 0:
        print("Please type a positive number")
        break
    else:
        inp = int(inp)
    