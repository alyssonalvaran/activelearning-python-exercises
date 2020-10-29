#!/usr/bin/env python
# coding: utf-8

# ## Exercise 9: Object-Oriented Programming

# #### products

# Create a class called `Product` with a constructor that contains the following attributes:
# * id (required)
# * description (required)
# * price (optional; default value is 0)

# In[1]:


class Product:
    
    def __init__(self, id, description, price = 0):
        self.id = id
        self.description = description
        self.price = price


# #### products-test

# Create 3 instances of `Product` and add them to a list named `products`.

# In[2]:


p1 = Product(101, "Coke Can", 25.00)
p2 = Product(208, "Lays Chips", 105.00)
p3 = Product(560, "Mott's Apple Juice", 200.00)

products = [p1, p2, p3]


# Iterate through `products` and display their attributes.

# In[3]:


for p in products:
    print("ID:", p.id)
    print("Description:", p.description)
    print("Price:", p.price)
    print()

