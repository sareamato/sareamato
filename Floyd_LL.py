#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time
import sys


# In[2]:


#linked list creation for test case
cols = [0,1,2]
df1 = pd.read_csv('Project2_Input_File3.csv', usecols = cols, header = 0)#import csv
index = df1.index
V = len(index)
#total amount of edges
n = len(pd.unique(df1['NodeID']))
#total amount of unique nodes / vertexes
start_node = df1['NodeID'].to_list()
start_node = map(str, start_node)
end_node = df1['ConnectedNodeID'].to_list()
weight = df1['Distance'].to_list()
edgeList = df1.values.tolist()
for i in edgeList:
    i[0] = int(i[0])
    i[1] = int(i[1])
linkedList = {}
for e in edgeList:
    if e[0] not in linkedList:
        linkedList[int(e[0])] = {}
    linkedList[int(e[0])].update({e[1] : e[2]})
    #floyd(linkedList)
    #print(linkedList)


# In[32]:


#Floyd Linked List
sys.getsizeof(linkedList)


# In[26]:


###Printing everything - not for use in time analysis
# def floyd_ll(graph, start, end):
#     dist = {}
#     P = {} 

#     for u in graph:
#         dist[u] = {}
#         P[u] = {}

#         for v in graph:
#             dist[u][v] = float('INF')
#             P[u][v] = -1
#             dist[u][u] = 0
#         for z in graph[u]:
#             dist[u][z] = graph[u][z]
#             P[u][z] = u
#     print('Path:')
#     for k in graph:
#         for i in graph:
#             for j in graph:
#                 if dist[i][k] + dist[k][j] < dist[i][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]
#                     P[i][j] = k
#                 if i == start and j == end:
#                     print(P[i][j])
#     print('Distance:')
#     print(dist[start][end])

    


# In[10]:


## main function to be used in time analysis, comment out printing the dist, remove the start and end inputs
def floyd_ll(graph, start, end):
    dist = {}


    for u in graph:
        dist[u] = {}


        for v in graph:
            dist[u][v] = float('INF')

            dist[u][u] = 0
        for z in graph[u]:
            dist[u][z] = graph[u][z]


    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print('Distance:')
    print(dist[start][end])


# In[11]:


floyd_ll(linkedList, 187, 68)


# In[5]:


def floyd_linked(csv):
    start_time = time.time()
    cols = [0,1,2]
    df1 = pd.read_csv(csv, usecols = cols, header = 0)#import csv
    index = df1.index
    V = len(index)
    #total amount of edges
    n = len(pd.unique(df1['NodeID']))
    #total amount of unique nodes / vertexes



    # LINKED LIST CREATION
    start_node = df1['NodeID'].to_list()
    start_node = map(str, start_node)
    end_node = df1['ConnectedNodeID'].to_list()
    weight = df1['Distance'].to_list()
    edgeList = df1.values.tolist()
    for i in edgeList:
        i[0] = int(i[0])
        i[1] = int(i[1])
    linkedList = {}
    for e in edgeList:
        if e[0] not in linkedList:
            linkedList[int(e[0])] = {}
        linkedList[int(e[0])].update({e[1] : e[2]})
    #floyd(linkedList)
    #print(linkedList)
    floyd(linkedList)
    elapsed_time = time.time() - start_time
    print(elapsed_time)


# In[8]:


floyd_linked('Project2_Input_File1.csv')


# In[9]:


floyd_linked('Project2_Input_File2.csv')


# In[10]:


floyd_linked('Project2_Input_File3.csv')


# In[11]:


floyd_linked('Project2_Input_File4.csv')


# In[12]:


floyd_linked('Project2_Input_File5.csv')


# In[13]:


floyd_linked('Project2_Input_File6.csv')


# In[14]:


floyd_linked('Project2_Input_File7.csv')


# In[15]:


floyd_linked('Project2_Input_File8.csv')


# In[16]:


floyd_linked('Project2_Input_File9.csv')


# In[17]:


floyd_linked('Project2_Input_File10.csv')


# In[ ]:




