#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ala_carte(x, y):
    if x< 0 and y > 0:
        result = 'negative'
    elif x > 0 and y < 0:
        result = 'negative'
    else: 
        result = 'positive'
    multiplier = abs(x)
    multiplicant = abs(y)
    list1 = [multiplier]
    list2 = [multiplicant]
    while multiplier >= 1:
        multiplier = multiplier/2
        list1.append(multiplier)

    for x in range (len(list1)):
        multiplicant = multiplicant*2
        list2.append(multiplicant)
    dict_a = dict(zip(list1, list2))
    #print(dict_a)
    list3 = []
    for key in dict_a:
        if(int(key)%2 != 0):
            list3.append(dict_a[key])
    total = sum(list3)
    
    if result == 'negative':
            print(-total)
    else:
        print(total)
  
             


# In[2]:


#Test Case 1 
ala_carte(7000, 7294)


# In[3]:


#Test Case 2 
ala_carte(25, 5038385)


# In[4]:


#Test Case 3 
ala_carte(-59724, 783)


# In[5]:


#Test Case 4 
ala_carte(8516, -82147953548159344)


# In[6]:


#Test Case 5 
ala_carte(45952456856498465985, 98654651986546519856)


# In[ ]:




