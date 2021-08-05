#!/usr/bin/env python
# coding: utf-8

# This code is for rectangular multiplication


import numpy as np
import math


# In[5]:


def rectangular (x,y):
    if x< 0 and y > 0:
        sign = 'negative'
    elif x > 0 and y < 0:
        sign = 'negative'
    else: 
        sign = 'positive'
    x = abs(x)
    y = abs(y)
    digits_x = [int(n) for n in str(x)]
    digits_y = [int(n) for n in str(y)]
    list1 = []
    list2 = []
    mat_even = []
    mat_odd = []
    result =[]
    size_x = len(digits_x)
    size_y = len(digits_y) 
    size = (size_y + size_x) + 1
    for k in digits_y:
        for j in digits_x:
            mult = j*k
            list1.append(str(mult).zfill(2))
    for l in list1:
        digits_mult = [int(n) for n in str(l)]
        list2.append(digits_mult[0])
        list2.append(digits_mult[1])
    mat = np.array(list2)
    for i in range (0, len(mat), 2):
        mat_even.append(mat[i])
        mat_even.append(0)
    for i in range (1, len(mat), 2):
        mat_odd.append(0)
        mat_odd.append(mat[i])
    n_odd = len(mat_odd) - 2
    n_even = len(mat_even) - 2
    while len(mat_odd) > 0 or len(mat_even) > 0:
        for j in range(size_x*2):
                result.append(mat_odd.pop())
        for i in range(size_x*2):
            result.append(mat_even.pop())
    #result = list(reversed(result))
    
    matrix = np.array(result).reshape( size_y*2, size_x *2)
    #print(matrix)
    rows = len(matrix)
    cols = len(matrix[0])
    diags = [[matrix[sum_-k][k]
          for k in range(sum_ + 1)
          if (sum_ - k) < rows and k < cols]
         for sum_ in range(rows + cols - 1)]
    n_diags = (len(diags))
    carryover = 0
    total = []
    answer = []
    for l in range(0, n_diags, 2):
        sum_a = sum(diags[l])
        if ((sum_a + carryover) >= 10):
            total.append((sum_a + carryover) % 10 )
            carryover = math.floor((sum_a + carryover) /10)
        else:
            total.append((sum_a + carryover) %10)
            carryover = 0
    for i in range(len(total) -1 , -1, -1):
        answer.append(total[i])
    if sign == 'negative':
        answer.insert(0, '-')
    for i in answer: 
        print(i, end="" ) 
       
            
    
             


# In[6]:


#Test Case 1 
rectangular(7000, 7294)


# In[7]:


#Test Case 2 
rectangular(25, 5038385)


# In[8]:


#Test Case 3 
rectangular(-59724, 783)


# In[9]:


#Test Case 4 
rectangular(8516, -82147953548159344)


# In[10]:


#Test Case 5 
rectangular(45952456856498465985, 98654651986546519856)


# In[ ]:




