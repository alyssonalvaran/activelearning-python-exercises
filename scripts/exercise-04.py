#!/usr/bin/env python
# coding: utf-8

# ## Exercise 4: Collections

# ### Major Step 1 - Working with Lists

# #### months-using-lists

# Create a list named `months` containing the months of the year in words.

# In[1]:


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


# Using a loop, print out the contents of the list.

# In[2]:


for month in months:
    print(month)


# #### product-list

# Ask the user to enter a month (1 to 12). Lookup the list and display the corresponding textual version of the month.

# In[3]:


# assuming that the user will enter an integer
num = int(input("Enter month (1 to 12): "))

if 1 <= num <= 12:
    print(str(num) + " is " + months[num - 1])
else:
    print("Please enter 1 to 12.")


# Ask the user for a product description. As the user enters products, add them to a list. Repeat until the user decides not to enter any more products. After the user has completed entering all the products, display the contents of the list.

# In[4]:


products = []
is_done = False

while not is_done:
    products.append(input("Enter description: "))
    
    # assuming that the user will only enter y or n
    if input("Do you want to enter another product? (y/n) ").lower() == "n":
        is_done = True
    
    print()

print("Here are the products you added:")
for product in products:
    print(product)


# ### Major Step 2 - Working with Dictionaries

# #### months-using-dictionaries

# Create a dictionary named `months` containing the months of the year in words as keys, and the numeric equivalent of the month as numbers.

# In[5]:


months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


# Using a loop, print out the contents of the dictionary.

# In[6]:


for month in months:
    print(month + " = " + str(months[month]))


# Ask the user to enter a month. Lookup the list and display the corresponding numerical version of the month.

# In[7]:


# assuming that the user will enter a valid input
month = input("Enter month: ")

if month in months:
    print(month + " is " + str(months[month]))


# #### products-dictionary

# Ask the user for a product code and a product description. As the user enters products, add them to a dictionary using code as keys and the descriptions as values. Repeat until the user decides not to enter any more products. After the user has completed entering all the products, display the contents of the dictionary.

# In[8]:


products = {}
is_done = False

while not is_done:
    code = input("Enter code: ")
    desc = input("Enter description: ")
    products[code] = desc
    
    # assuming that the user will only enter a valid input
    continue_shopping = input("Do you want enter another product? (y/n) ").lower()
    if continue_shopping == "n":
        is_done = True
    
    print()

print("Here are the products you entered:")

for code, desc in products.items():
    print()
    print("Code: " + code)
    print("Description: " + desc)

