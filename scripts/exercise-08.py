#!/usr/bin/env python
# coding: utf-8

# ## Exercise 8

# #### dates-and-times

# Ask the user to input a month, day, and year, and display it in the following format - `Jan 2, 2019 (Wed)`.

# In[1]:


import datetime

# assuming that the user will enter valid inputs:
month = int(input("Enter month (1 to 12): "))
day = int(input("Enter day (1 to 31): "))
year = int(input("Enter year (1 to 12): "))

dt = datetime.date(year, month, day)

print("That is " + f"{dt:%A} {dt:%B} {dt.day}, {dt:%Y}")


# Display the current time in the following format - `9:05 PM`.

# In[ ]:


today = datetime.datetime.today()
print(f"{today.hour}:{today:%M} {today:%p}")


# #### list-dir

# Display the contents of the root directory.

# In[ ]:


import os

for file in os.listdir("/"):
    print(file)

