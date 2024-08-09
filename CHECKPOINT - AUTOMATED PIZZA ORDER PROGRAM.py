#!/usr/bin/env python
# coding: utf-8

# In[6]:


name = input("What's your name? ")


# In[8]:


print(f"Hello, {name}")


# In[2]:


print("Welcome to Python Pizza Deliveries")
size = input("what size of pizza will you be having? S, M, L: ")
add_pepperoni = input("would you like pepperoni on your pizza? Y, N: ")
extra_cheese = input("would you want extra cheese on your pizza? Y, N: ")

bill = 0  #I need to assign bill to a base value so bill becomes incremental based on order request

if size == 'S':
    bill += 15       #+= ---> Add & Assign operator
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
    
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
        
if extra_cheese == 'Y':
    bill += 1
    
print(f"final bill is: ${bill}")

