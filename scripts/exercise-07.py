#!/usr/bin/env python
# coding: utf-8

# ## Exercise 7: Modules

# Create a module named `password_utils` and copy the `get_password_score(password)` function from Exercise 6.

# Modify `password_strength.py` to make use of the `get_password_score(password)` function from `password_utils`.

# In[1]:


import password_utils

password = input("Enter a word: ")
score, strength = password_utils.get_password_score(password)
    
print("Total score: " + str(score))
print("Password strength: " + strength)

