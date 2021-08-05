#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd
import time
import sys


# In[41]:


import memory_profiler 
get_ipython().run_line_magic('load_ext', 'memory_profiler')


# In[66]:


cols = [0,1,2]
df1 = pd.read_csv('Project2_Input_File3.csv', usecols = cols, header = 0)#import csv
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
    i[0] = str(i[0])
    i[1] = str(i[1])
linkedList = {}
for e in edgeList:
    if e[0] not in linkedList:
        linkedList[e[0]] = {}
    linkedList[e[0]].update({e[1] : e[2]})


# In[68]:


#Dijkstra's LL
sys.getsizeof(linkedList)


# In[69]:


def Dijkstra(graph, start, end = None):
    #end point - optional, set at None for time analysis to visit all destinations
    
    #mark all nodes as unvisited
    unvisited = list(graph)
    # Initialize dictionary of shortest distances
    D = dict()
    for v in unvisited:
        D[v] = [[],float('inf')]
   
    # Zero distance
    D[start][1] = 0.0
    # While not all vertices have been yet visited
    while len(unvisited) > 0:
       
        minD, curr = min([(D[n][1],n) for n in unvisited])
        # Add node to path
        D[curr][0].append(curr)
        # at dest
        if curr == end:
            return end, D[end]
        # Loop over all vertices - neighbors
        for n, d in graph[curr].items():
            # if n has not been visited
            if n in unvisited:
                # compute distance to this neighbor through current vertex
                currd = minD + d
                # check if this distance is less than currently assigned
                # tentative distance
                if currd < D[n][1]:
                    # re-assign shortest distance
                    D[n][1] = currd
                    # shortest path to this vertex is through current vertex
                    D[n][0] = D[curr][0][:]
                # endif #
            # endif #
        # endfor #
        # Remove current node from unvisited ones
        unvisited.remove(curr)
    # endwhile #
    return D


# In[71]:


Dijkstra(linkedList, '197', end = '27')


# In[72]:


Dijkstra(linkedList, '65', end = '280')


# In[73]:


Dijkstra(linkedList, '187', end = '68')


# In[76]:



def dijk_linked(csv):
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
        i[0] = str(i[0])
        i[1] = str(i[1])
    linkedList = {}
    for e in edgeList:
        if e[0] not in linkedList:
            linkedList[e[0]] = {}
        linkedList[e[0]].update({e[1] : e[2]})
        
    list1 = list(linkedList)
    for i in list1:
        Dijkstra(linkedList, i, end = None)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
        


# In[77]:


dijk_linked('Project2_Input_File1.csv')


# In[46]:


dijk_linked('Project2_Input_File2.csv')


# In[47]:


dijk_linked('Project2_Input_File3.csv')


# In[48]:


dijk_linked('Project2_Input_File4.csv')


# In[49]:


dijk_linked('Project2_Input_File5.csv')


# In[50]:


dijk_linked('Project2_Input_File6.csv')


# In[52]:


dijk_linked('Project2_Input_File7.csv')


# In[51]:


dijk_linked('Project2_Input_File8.csv')


# In[53]:


dijk_linked('Project2_Input_File9.csv')


# In[54]:


dijk_linked('Project2_Input_File10.csv')


# In[55]:


get_ipython().run_line_magic('memit', "dijk_linked('Project2_Input_File1.csv')")


# In[ ]:




