#!/usr/bin/env python
# coding: utf-8

# ### Sara Amato: Project 1

# Design and implement your own algorithm that takes the array A with size m+n as input where:
# 
# Subarray A[1], A[2],...A[m] sorted in ascending order
# Subarray A[m+1], A[m+2],...A[n] sorted in ascending order
# and merges the two subarrays using an auxiliary array Aux of size min {m, n} back into array A sorted in ascending order. You must design and implement your own sorting function. Use of sorting functions in libraries is not permitted.

# In[1]:


import numpy as np


# In[2]:


def prob1(x, y):
    x_size = len(x)
    y_size = len(y)
    m = x_size
    l = y_size
    n = m + l
    aux = [0]* n
    np.array(aux)
    A = x+y
    np.array(A)
    mid = A[m]
    i = 0
    j = 0
    k = 0
    A = []
    while i< m and j< l:
        if x[i] < y[j]:
            aux[k] = x[i]
            k = k +1
            i = i +1
        else:
            aux[k] = y[j]
            k = k +1
            j = j +1
    while i < m:
        aux[k] = x[i]
        k = k +1
        i = i +1
    while j < l:
        aux[k] = y[j]
        k = k +1
        j = j +1
    
    for i in range (n):
        A.append (aux[i])
        #A =  aux[i]
    print (A)


# In[3]:


#Test Case 1: 
prob1([] ,[3, 7, 9])


# In[4]:


#Test Case 2
prob1([2,7,8], [1])


# In[5]:


#Test Case 3
prob1([1, 7, 10, 15], [3, 8, 12, 18])


# In[6]:


#Test Case 4
prob1([1, 3, 5, 5, 15, 18, 21], [5, 5, 6, 8, 10, 12, 16, 17, 17, 20, 25, 28])

