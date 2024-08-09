#!/usr/bin/env python
# coding: utf-8

# ### Step 1: Creating a list to store the shopping item

# In[ ]:


shopping_list = []

'''Use a while loop to create a menu of options for the user to add, 
remove, or view items from the list'''

while True:
    print("Hello would you like to:\nAdd an item \nRemove an item \nView your list of items")
    action = input("To add item enter Add\nTo remove item enter Remove\nTo View your list of items enter View")
    if action == "add":
             item_name=input('what item would you like to add?')
             shopping_list.append(item_name)
             for items in range(1,11):
                        if items==10 and len(shopping_list)>items:
                            raise Exception("Maximum amount of items exceeded")
                        else:
                            pass       
    elif action=='remove':
        item_name=input('which item would you like to remove?')
    elif action=='view':
        for items in shopping_list:
            print(items)
    else:
        break
                    
                
            
                
                
            


