#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import queue
import numpy as np
import sys


# In[43]:


#def merge(csv1, csv2):
cols = [0,1,2,3]
    #include coordinates to identify duplicates
df1 = pd.read_csv('Project3_G1_Data.csv',usecols = cols, header = 0)#import csv
df2 = pd.read_csv('Project3_G2_Data.csv', usecols = cols, header = 0)
    #print(df1)
    #print(len(df2))
    #these are the duplicates that will be deleted from df2 
drop_list = []
   #duplicate identification
for i in range(len(df1)):
    for k in range(len(df2)):
        if df1.iloc[i ,2] == df2.iloc[k,2]:
                #if the distance is the same
                #and the coordinates are the same
            if df1.iloc[i ,3] == df2.iloc[k,3]:
                    drop_list.append(k)
    #drop list must drop the highest index to lowest so the index isn't affected by removing one 
drop_list.sort(reverse=True)
df2_clean = df2.drop(drop_list)
    
    #the node ids need to be relabeled because it will not be the correct adjacency matrix if there are two node ids of the same value that correspond to different paths
node_id = df1['NodeID']
max_value = node_id.max()
max_value = max_value+1
    #print(max_value)
for i in range(len(df2_clean)):
    x = df2_clean.iloc[i, 0]
    y = df2_clean.iloc[i, 1]
    df2_clean.iloc[i,0]  = x+ max_value
        #print(df2_clean.iloc[i,0])
    df2_clean.iloc[i,1] = y + max_value
        #print(df2_clean.iloc[i,1])
    #print(df2_clean)

    
    #these are the two df to be merged
frames = [df1, df2_clean]
    #concat the dfs together

df_merged_allcols = pd.concat(frames,  ignore_index = True)
    #print(df_merged)


df_merged_clean = df_merged_allcols[['NodeID', 'ConnectedNodeID', 'Distance']]
    #return df_merged_clean

    
index = df_merged_clean.index
V = len(index)
            #total amount of edges
n2 = len(pd.unique(df_merged_clean['NodeID']))
            #total amount of unique nodes / vertexes
n = len(df_merged_clean)
INF = float('inf') 
   
#print(n)
#print(V)
#print(n2)
     # MATRIX CREATION
G = (np.ones((n2+4, n2+4), dtype = int))*INF
dist = (np.ones((n2+4, n2+4), dtype = int))*INF
for x in range(0, n):
    distance = df_merged_clean.at[int(x), 'Distance']
    row = df_merged_clean.at[int(x), 'NodeID']
    col = df_merged_clean.at[int(x), 'ConnectedNodeID']
    G[row,col] = distance
    
    
#G in edge list format
list1 = []
for i in range(len(G)):
#for i in range rows
    for j in range(len(G[0])):
    #for j in range columns
        if G[i,j] != INF:
            list1.append([str(i),str(j), G[i,j]] )
#print(list1)

#deleting blank duplicate columns
G = np.delete(G, [2000,1959,1916,1910], axis = 1)

#deleting duplicate row
G = np.delete(G, [2000,1959,1916,1910], axis = 0)


# In[48]:


def kruskal_array(G): 
    print('FromNode, ToNode, Distance')
    minimum = 0 # Cost of min MST 
  
    # Initialize sets of disjoint sets 
    for i in range(V): 
        parent[i] = i 
  

    edges = 0
    #initiate edge count at 0
    #goes through each edge one by one
    while edges < (V - 2): 
        min = INF 
        node1 = -1
        node2 = -1
        for i in range(V): 
            for j in range(V): 
                if find(i) != find(j) and G[i][j] < min: 
                    min = G[i][j] 
                    node1 = i 
                    node2 = j 
        
        union(node1, node2) 
        print( node1,',',     node2,',',      min) 
        edges = edges+ 1
        #add one to edge count
        minimum += min
  
    print('Total distance') 
    print(minimum)

def union(i, j): 
    k = find(i) 
    l = find(j) 
    parent[k] = l 

def find(i): 
    while parent[i] != i: 
        i = parent[i] 
    return i 
  

  


# In[49]:


V = len(G)
parent = [i for i in range(V)] 
INF = float('inf') 

  
# Print the solution  
kruskal_array(G) 


# In[ ]:




