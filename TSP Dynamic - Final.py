#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import itertools
from itertools import permutations


# In[2]:


cols = [0,1,2]
df1 = pd.read_csv('Project 4_Problem 2_InputData.csv', usecols = cols, header = 0)#import csv
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
#print(matrix)


# In[6]:


def tsp_dynamic_2d(matrix):

    n = len(matrix)
    #This will keep the distances
    Distance = {}
    for k in range(1, n):
        #left shift, reassign
        Distance[(1 << k, k)] = (matrix[0][k], 0)
    #Dynamic Programming
    for c in range(2, n):
        #all combinations
        for s in itertools.combinations(range(1, n), c):
            # cost
            costs = 0
            for cost in s:
                costs |= 1 << cost
            for k in s:
                previous = costs & ~(1 << k)
                final_distance = []
                for m in s:
                    if m == 0 or m == k:
                        continue
                    #print(dists[m][k])
                    final_distance.append((Distance[(previous, m)][0] + matrix[m][k], m))
                Distance[(costs, k)] = min(final_distance)
    costs = (2**n - 1) - 1
    # Calculate optimal cost
    final_distance = []
    for k in range(1, n):
        final_distance.append((Distance[(costs, k)][0] + matrix[k][0], k))
    opt, parent = min(final_distance)
    path = [0]
    for i in range(n - 1):
        path.append(parent)
        new = costs & ~(1 << parent)
        _, parent = Distance[(costs, parent)]
        costs = new
    # Add 0 since we start there
    path.append(0)
    #Print out the final results
    print('distance:', opt)
    print('path:', path)



# In[7]:


tsp_dynamic_2d(matrix)


# In[3]:


matrix1 = np.array(matrix)
col = len(matrix1)
#print(col)
lower_triangle = (matrix1[np.tril_indices(24, k = -1)])
print(lower_triangle)


# In[ ]:


def tsp_dynamic_1d(array, n): 
    start = 0
    # keep all nodes
    nodes = [] 
    for i in range(n): 
        if i != start: 
            nodes.append(i) 

    mincost = 999999999
    
    nextnode = permutations(nodes)
    path = []
    
    for i in nextnode:
        # store current path cost
        currdist = 0
        
        # procress current path weight 
        k = start 
        for j in i: 
            spot = int(((k *(k-1))/2)+j)

            currdist += array[spot] 
            k = j 
        spot = int(((k *(k-1))/2)+start)
        currdist += array[spot] 
        #if the distance is less than the current minimum
        if currdist < mincost:
            mincost = currdist
            path = [start]
            path.extend(list(i))
            path.append(start)
            
            
    print("DISTANCE:", mincost)
    print('PATH :',path)
    



# In[ ]:


tsp_dynamic_1d(lower_triangle,24)


# In[ ]:




