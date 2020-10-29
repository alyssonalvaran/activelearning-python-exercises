#!/usr/bin/env python
# coding: utf-8

# ## Exercise 2: Basic Python Syntax

# #### Answer the following questions:

# In[1]:


1 + 1


# In[2]:


"1" + "1"


# In[3]:


1 + "1"


# In[4]:


1 + True


# In[5]:


"1" + True


# In[6]:


1 + None


# #### Answer true or false on the questions below:

# In[7]:


1 == '1'


# In[8]:


1 == True


# In[9]:


False == None


# In[10]:


"apple" < "Umbrella"


# #### variables
# Print out the variable names together with the values.

# In[11]:


quantity = 23
print("quantity =", quantity)

price = 16.5
print("price =", price)

is_paid = False
print("is_paid =", is_paid)

message = "Thank you!"
print("message =", message)


# #### numbers
# Ask for 3 numbers and display the sum, product, and average of the three inputted numbers.

# In[12]:


# assuming that the user will only enter valid inputs
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

print()
print("Sum = %g" % (num1 + num2 + num3))
print("Product = %g" % (num1 * num2 * num3))
print("Average = %g" % ((num1 + num2 + num3) / 3))


# #### c2f
# Ask the user for a temperature in Celsius. Convert this to Fahrenheit.

# In[13]:


# assuming that the user will only enter valid inputs
c = float(input("Enter temperature in Celsius: "))
f = c * 9 / 5 + 32

print(str(c) + " Celsius = " + str(f) + " Fahrenheit")

