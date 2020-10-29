#!/usr/bin/env python
# coding: utf-8

# ## Exercise 3.2: Loops

# ### Major Step 1 - Using a for loop

# #### factorial
# Ask the user for a number and display its factorial.

# In[1]:


# assuming that the user will only enter integers
num = int(input("Enter a number: "))

if num == 0:
    factorial = 1
    print("The factorial of %d is %d." % (num, factorial))
else:
    factorial = num
    for i in range(1, num):
        factorial = factorial * i
    print("The factorial of %d is %d." % (num, factorial))


# #### right-triangle
# Ask the user for a number and print a right angle triangle with each row displaying the row number.

# ### Major Step 2 - Using a while loop

# In[2]:


# assuming that the user will only enter integers
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(i):
        print(i, end="")
    print()


# You can also do this using a single for loop:

# In[3]:


for i in range(1, num + 1):
    print(str(i) * i)


# Modify any of the exercises you have completed to ask the user if he/she wants to try again. Once the user decides not to try again, greet the user with the message "Have a good day".

# In[4]:


try_again = True

while try_again:
    num = int(input("Enter a number: "))

    for i in range(1, num + 1):
        print(str(i) * i)
    
    # assuming that the user will only enter y or n
    if input("\nWould you like to try again? (y/n): ").lower() == "n":
        try_again = False
        print("Have a good day!")

