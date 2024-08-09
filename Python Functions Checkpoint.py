#!/usr/bin/env python
# coding: utf-8

# In[38]:


def add(a,b):
    return a + b
    
def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

operations = {'+' : add,
             '-' : subtract,
             '*' : multiply,
             '/' : divide}

def calculator():
    num1 = float(input("Enter the first number: "))

    for symbol in operations.keys():
        print(symbol)
                                                                                                        
    should_continue = True
    
    while should_continue:
        ops_symbol = input("Enter operations symbol (or 'exit' to quit): ")
        num2 = float(input("Enter the second number: "))
    
       
        
        if ops_symbol in operations:
           

            calculation_function = operations[ops_symbol]

            answer = calculation_function(num1, num2)
        
            print(f'The result of {num1} {ops_symbol} {num2} is: {answer}')

            should_continue = input("would you like to continue with this result as you first number (yes/no):  ")

            if should_continue == 'yes':
                num1 = answer
            elif should_continue == 'no':
                should_continue = False
    
calculator()
    
                
    



# In[ ]:




