#!/usr/bin/env python
# coding: utf-8

# ## Exercise 3.1: Conditional Statements

# #### days-in-month
# Ask the user for the month (1 to 12). After the user has selected a month, output the number of days in that. If the user enters an invalid month, print an error to the screen. You can choose to ignore leap years for now.

# In[1]:


month = input("Enter month (1 to 12): ")

if month == "1":
    print("There are 31 days.")
elif month == "2":
    print("There are 28 days.")
elif month == "3":
    print("There are 31 days.")
elif month == "4":
    print("There are 30 days.")
elif month == "5":
    print("There are 31 days.")
elif month == "6":
    print("There are 30 days.")
elif month == "7":
    print("There are 31 days.")
elif month == "8":
    print("There are 31 days.")
elif month == "9":
    print("There are 30 days.")
elif month == "10":
    print("There are 31 days.")
elif month == "11":
    print("There are 30 days.")
elif month == "12":
    print("There are 31 days.")
else:
    print("Please enter a number between 1 to 12.")


# Modify the previous exercise so that the text version of the month (2 = February) is also displayed in the output.

# In[2]:


month = input("Enter month (1 to 12): ")

if month == "1":
    print("There are 31 days in January.")
elif month == "2":
    print("There are 28 days in February.")
elif month == "3":
    print("There are 31 days in March.")
elif month == "4":
    print("There are 30 days in April.")
elif month == "5":
    print("There are 31 days in May.")
elif month == "6":
    print("There are 30 days in June.")
elif month == "7":
    print("There are 31 days in July.")
elif month == "8":
    print("There are 31 days in August.")
elif month == "9":
    print("There are 30 days in September.")
elif month == "10":
    print("There are 31 days in October.")
elif month == "11":
    print("There are 30 days in November.")
elif month == "12":
    print("There are 31 days in December.")
else:
    print("Please enter a number between 1 to 12.")


# #### smallest
# Ask for three numbers from the user and print the greatest number.

# In[3]:


# assuming that the user will only input integers
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

greatest_num = num1
if num2 > greatest_num:
    greatest_num = num2
if num3 > greatest_num:
    greatest_num = num3

print()
print("The greatest of the 3 numbers is", greatest_num)

