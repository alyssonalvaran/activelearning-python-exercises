#!/usr/bin/env python
# coding: utf-8

# ## Exercise 12: Exceptions

# Modify `ProductsService`'s `find()` method so that instead of returning `None` when a product is not found, a `Lookup` error is raised.

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
    def find(cls, id):
        output = None
        for product in cls.products:
            if id == product.id:
                output = product
        if output == None:
            raise LookupError("That product doesn't exist.")
        else:
            return output


# Modify `products-service-test.py` so that when a `LookupError` occurs, the message "That product doesn't exist" is displayed.

# In[2]:


# copied from products-service-test.py
# assuming that the user will enter a valid input
id = int(input("Enter a product ID: "))

try:
    product = ProductsService.find(id)
    
    print("Description:", product.description)
    print("Price:", product.price)
except LookupError as e:
    print(e)


# In `products.py`, create your own exception type called `ProductNotFoundException` whose default error message is "That product doesn't exist". Modify `ProductsService`'s `find()` method so that your `ProductNotFoundException` is raised instead of `LookupError`.

# In[3]:


class ProductNotFoundException(BaseException):
    def __init__(self, message="That product doesn't exist."):
        self.message = message
        super(ProductNotFoundException, self).__init__(self.message)

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
    def find(cls, id):
        output = None
        for product in cls.products:
            if id == product.id:
                output = product
        if output == None:
            raise ProductNotFoundException()
        else:
            return output


# Modify `products-service-test.py` to handle `ProductNotFoundException` instead of `LookupError`.

# In[4]:


# copied from products-service-test.py
# assuming that the user will enter a valid input
id = int(input("Enter a product ID: "))

try:
    product = ProductsService.find(id)
    
    print("Description:", product.description)
    print("Price:", product.price)
except ProductNotFoundException as e:
    print(e)

