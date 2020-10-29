#!/usr/bin/env python
# coding: utf-8

# ## Exercise 10: Decorators

# #### products

# Create a class called `ProductsService` which contains:
# * a static attribute called `products` which contains a list of 3 Product instances
# * a class method called `get_products()` which returns `products`.
# * a class method called `find()` which accepts `id` as a parameter and returns either a `Product` object that matches the parameter or `None`.

# In[1]:


# copied from products.py
class Product:
    
    def __init__(self, id, description, price = 0):
        self.id = id
        self.description = description
        self.price = price

class ProductsService:
    products = [
        Product(101, "Coke Can", 25.00),
        Product(208, "Lays Chips", 105.00),
        Product(560, "Mott's Apple Juice", 200.00)
    ]
    
    @classmethod
    def get_products(cls):
        return cls.products
    
    @classmethod
    def find(cls, id):
        for product in cls.products:
            if id == product.id:
                return product
        
        return None


# #### products-service-test

# Use `ProductsService`'s `get_products()` to retrieve the list of products. Iterate through the list and print its attributes.

# In[2]:


products = ProductsService.get_products()

for product in products:
    print("ID:", product.id)
    print("Description:", product.description)
    print("Price:", product.price)
    print()


# Ask the user for a product id. Use `ProductsService`'s `find()` method to retrieve the product and display its attributes. If the product id entered does not exist, display "That product doesn't exist".

# In[3]:


# assuming that the user will enter a valid input
id = int(input("Enter a product ID: "))
product = ProductsService.find(id)

if product is not None:
    print("Description:", product.description)
    print("Price:", product.price)
else:
    print("That product doesn't exist.")

