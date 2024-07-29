#!/usr/bin/env python
# coding: utf-8

# # Mini Restaurant Menu Project

# In[2]:


menu = {'pizza': 50,
        'burger': 40,
        'pasta': 50,
        'coffee': 80,
        'salad': 40
       }
print(menu)


# In[4]:


# greeting
print("Welcome to python restaurant")
print("pizza: 50\nburger:40\npasta: 50\ncoffee:80\nsalad: 40")


# In[20]:


order_total = 0

item_1 = input("Enter the name of item that you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")
    
another_order = input("Do you want to add another item? (yes/no): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available")

print(f"Total amount to pay is {order_total}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




