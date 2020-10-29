#!/usr/bin/env python
# coding: utf-8

# ## Exercise 6: Functions

# #### days-in-month

# Modify days-in-month of Exercise 3.1. Write a function called `num_days_in_month(month)` which will return the number of days given a month (1 to 12). The function should return -1 if the value passed is not between 1 to 12. Modify the code to make use of the function.

# In[1]:


def num_days_in_month(month):
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month)
    else:
        return -1, ""
    
    days = 31
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    
    if month == 2:
        days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    
    return days, months[month - 1]

month = input("Enter month (1 to 12): ")
days, str_month = num_days_in_month(month)

if days != -1:
    print("There are {} days in {}.".format(days, str_month))
else:
    print("Please enter a number between 1 to 12.")


# #### password-strength

# Modify password-strength of Exercise 4. Write a function called `get_password_score(password)` which will return the password score. Modify the code to make use of the function.

# In[2]:


def get_password_score(password):
    score = 0
    strength = "Low"
    
    for letter in password:
        # The numeric equivalent of A-Z in the ASCII table is 65-90
        # while the numeric equivalent of 0-9 in the ASCII table is 48-57
        if 65 <= ord(letter) <= 90 or 48 <= ord(letter) <= 57:
            score = score + 2

    if len(password) > 7:
        score = score + 2
        
    if 4 <= score < 10:
        strength = "Medium"
    elif score >= 10:
        strength = "High"

    return score, strength

password = input("Enter a word: ")
score, strength = get_password_score(password)
    
print("Total score: " + str(score))
print("Password strength: " + strength)

