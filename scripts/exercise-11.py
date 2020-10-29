#!/usr/bin/env python
# coding: utf-8

# ## Exercise 11: Inheritance and Polymorphism

# In the `Product` class, override the `__str__()` method to return the string representation of the product.

# In[1]:


# copied from products.py
class Product:
    
    def __init__(self, id, description, price = 0):
        self.id = id
        self.description = description
        self.price = price
    
    def __str__(self):
        output = output + "ID: " + str(self.id) + "\n"
        output = output + "Description: " + str(self.description) + "\n"
        output = output + "Price: " + str(self.price) + "\n"
        
        return output


# Modify `products-test.py` so that the product instances are printed instead of the individual attributes of the instances.

# In[2]:


# copied from products-test.py
p1 = Product(101, "Coke Can", 25.00)
p2 = Product(208, "Lays Chips", 105.00)
p3 = Product(560, "Mott's Apple Juice", 200.00)

products = [p1, p2, p3]

for product in products:
    print(product)


# Make the `products` attribute of `ProductsService` class private.

# In[3]:


# copied from products.py
class ProductsService:
    __products = [
        Product(101, "Coke Can", 25.00),
        Product(208, "Lays Chips", 105.00),
        Product(560, "Mott's Apple Juice", 200.00)
    ]


# Try accessing the `products` attribute directly using the class name.

# In[4]:


products = ProductsService.__products

