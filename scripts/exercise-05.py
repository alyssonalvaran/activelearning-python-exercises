#!/usr/bin/env python
# coding: utf-8

# ## Exercise 5: Strings

# #### password-strength

# Ask the user for a word. After which, print out that word letter by letter.
# 
# For each iteration, have an if statement that would determine a score for each character.
# - A capital letter: 2 points
# - A number: 2 points
# 
# Add up the total score, plus an additional 2 points if the inputted string is more than 7 characters long. Output the total score.
# 
# Output the strength of the password based on the following criteria:
# - score < 4: Low
# - 4 <= score < 10: Medium
# - score >= 10: High

# In[1]:


word = input("Enter a word: ")
score = 0
password_strength = "Low"

for letter in word:
    print(letter)
    
    # The numeric equivalent of A-Z in the ASCII table is 65-90
    # while the numeric equivalent of 0-9 in the ASCII table is 48-57
    if 65 <= ord(letter) <= 90 or 48 <= ord(letter) <= 57:
        score = score + 2

if len(word) > 7:
    score = score + 2
    
print("Total score: " + str(score))

if 4 <= score < 10:
    password_strength = "Medium"
elif score >= 10:
    password_strength = "High"

print("Password strength: " + password_strength)

