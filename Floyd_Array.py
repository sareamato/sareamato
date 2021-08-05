#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time
import sys


# In[2]:


cols = [0,1,2]
df1 = pd.read_csv('Project2_Input_File3.csv', usecols = cols, header = 0)#import csv
index = df1.index
V = len(index)
        #total amount of edges
n2 = len(pd.unique(df1['NodeID']))
        #total amount of unique nodes / vertexes
n = len(df1)



        # MATRIX CREATION
matrix = (np.ones((n2, n2), dtype = int))*99999999
dist = (np.ones((n2, n2), dtype = int))*999999999
for x in range(0, n):
    distance = df1.at[int(x), 'Distance']
    row = df1.at[int(x), 'NodeID']
    col = df1.at[int(x), 'ConnectedNodeID']
    matrix[row,col] = distance
matrix2 = matrix.tolist()
graph = matrix2
#floyd_mat(matrix)


# In[294]:


#Floyd matrix
sys.getsizeof(matrix)


# In[ ]:


###Printing everything - not for use in time analysis, print test case
# def path (P, q, r):
#     print('Distance:')
#     print(D[q,280])
#     if P[q,r] != 0:
#         path(P,q, P[q,r])
#         print(P[q,r])
#         path(P,P[q,r], r)
    
# def floyd_mat(D, start, end):
#     P = D
#     n = len(D)
#     for i in range(n):
#         for j in range(n):
#             P[i,j] = 0
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if D[i,k] + D[k,j]< D[i,j]:
#                     D[i,j] = D[i,k]+ D[k,j]
#                     P[i,j] = k
#     print('Distance:')
#     print(D[start,end])
#     print('Path')
#     path(P, start,end)


# In[12]:


###Print distance - main function - use in time analysis
    
def floyd_mat(D, start, end):
    n = len(D)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i,k] + D[k,j]< D[i,j]:
                    D[i,j] = D[i,k]+ D[k,j]
    print('Distance:')
    print(D[start,end])
    


# In[13]:


floyd_mat(matrix, 187, 68)


# In[15]:


def floyd_array(csv):
    start_time = time.time()
    cols = [0,1,2]
    df1 = pd.read_csv(csv, usecols = cols, header = 0)#import csv
    index = df1.index
    V = len(index)
        #total amount of edges
    n2 = len(pd.unique(df1['NodeID']))
        #total amount of unique nodes / vertexes
    n = len(df1)



        # MATRIX CREATION
    matrix = (np.ones((n2, n2), dtype = int))*99999999
    dist = (np.ones((n2, n2), dtype = int))*999999999
    for x in range(0, n):
        distance = df1.at[int(x), 'Distance']
        row = df1.at[int(x), 'NodeID']
        col = df1.at[int(x), 'ConnectedNodeID']
        matrix[row,col] = distance
    matrix2 = matrix.tolist()
    graph = matrix2
    floyd_mat(matrix)
    elapsed_time = time.time() - start_time
    print(elapsed_time)


# In[16]:


floyd_array('Project2_Input_File1.csv')


# In[5]:


floyd_array('Project2_Input_File2.csv')


# In[6]:


floyd_array('Project2_Input_File3.csv')


# In[7]:


floyd_array('Project2_Input_File4.csv')


# In[8]:


floyd_array('Project2_Input_File5.csv')


# In[9]:


floyd_array('Project2_Input_File6.csv')


# In[10]:


floyd_array('Project2_Input_File7.csv')


# In[11]:


floyd_array('Project2_Input_File8.csv')


# In[12]:


floyd_array('Project2_Input_File9.csv')


# In[13]:


floyd_array('Project2_Input_File10.csv')


# In[ ]:




