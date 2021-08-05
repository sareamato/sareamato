#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd
import numpy as np
import time
import sys


# In[4]:



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
  


# In[98]:


#Dijkstras array
sys.getsizeof(matrix)


# In[91]:


def printPath(path, j): 
    if path[j] == -1 :  
        print (j) 
        return
    printPath(path , path[j]) 
    print (j)
def print_all(D, path, end):
    print('Distance:')
    print(D[end])
    print('Path:'  )
    printPath(path, path[end])
    print(end)
    
        
        
def Dijkstra_matrix(matrix, start, end = None):
    #the end point is optional - this is importnat for the time analysis part. it should be set to none unless running a test case
   
    x = len(matrix)
    unvisited = []
    for i in range(x):
        unvisited.append(i)
    #the row
    y = len(matrix[0])
    #the column
    # D = shortest diff
    D =  [99999] * x
    #print(D)
    path = [-1] * x
    #for printing
    D[start] = 0
    # Not all vertices have been yet visited
    while len(unvisited) > 0:
        # current node
        min_index = -1
        minimum = 999999
  
        for i in range(len(D)): 
            if D[i] < minimum and i in unvisited: 
                minimum = D[i] 
                min_index = i 
        curr = min_index
        unvisited.remove(curr)

        for i in range(y):
            if matrix[curr][i] and i in unvisited:
                #n must be unvisited
                if D[curr] + matrix[curr][i] < D[i]:
                    D[i] = D[curr] + matrix[curr][i]
                    path[i] = curr

    print_all(D, path, end)              
    # endwhile #
    #return D
    #print(D[a_d] )


# In[92]:


Dijkstra_matrix(matrix, 197, 127)


# In[93]:



def Dijkstra_matrix(matrix, start, end = None):
    #the end point is optional - this is importnat for the time analysis part. it should be set to none unless running a test case
   
    x = len(matrix)
    unvisited = []
    for i in range(x):
  unvisited.append(i)
    #the row
    y = len(matrix[0])
    #the column
    # D = shortest diff
    D =  [99999] * x
    #print(D)
    path = [-1] * x
    #for printing
    D[start] = 0
    # Not all vertices have been yet visited
    while len(unvisited) > 0:
  # current node
  min_index = -1
  minimum = 999999
  
  for i in range(len(D)): 
      if D[i] < minimum and i in unvisited: 
          minimum = D[i] 
          min_index = i 
  curr = min_index
  unvisited.remove(curr)

  for i in range(y):
      if matrix[curr][i] and i in unvisited:
          #n must be unvisited
          if D[curr] + matrix[curr][i] < D[i]:
              D[i] = D[curr] + matrix[curr][i]
              path[i] = curr

    print_all(D, path, end)              
    # endwhile #
    #return D
    #print(D[a_d] )
    #print_all(D, path, a_d)              
    # endwhile #
    #return D
    #print(D[a_d] )


# In[94]:


def dijk_array(csv):
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
    for i in range(0, n2):
        Dijk_matrix(matrix, i, a_d = None)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    


# In[95]:


dijk_array('Project2_Input_File1.csv')


# In[80]:


dijk_array('Project2_Input_File2.csv')


# In[81]:


dijk_array('Project2_Input_File3.csv')


# In[82]:


dijk_array('Project2_Input_File4.csv')


# In[83]:


dijk_array('Project2_Input_File5.csv')


# In[84]:


dijk_array('Project2_Input_File6.csv')


# In[85]:


dijk_array('Project2_Input_File7.csv')


# In[86]:


dijk_array('Project2_Input_File8.csv')


# In[87]:


dijk_array('Project2_Input_File9.csv')


# In[88]:


dijk_array('Project2_Input_File10.csv')


# In[ ]:




