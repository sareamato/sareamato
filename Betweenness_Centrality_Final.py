#!/usr/bin/env python
# coding: utf-8

# Calculated betweeness centrality by hand using intersections in Pittsburgh



import pandas as pd

import collections


# In[2]:


cols = [0,1,2]
df1 = pd.read_csv('Project 4_Problem 1_InputData.csv', usecols = cols, header = 0)#import csv
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


# In[3]:


def Dijkstra(graph, start, end = None):
    list1 = list(linkedList)
    #end point - optional, set at None for time analysis to visit all destinations
    n = len(graph)
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
    values = D.values()
    values_list = list(values)
    #print(values_list)
    values_list_2 = []
    just_nodes = []
    for i in values_list:
        x = 0
        for j in i:
            if x == 0:
                values_list_2.append(j)
                x = x+1
    for i in values_list_2:
        x = 0
        for j in i:
                just_nodes.append(int(j))
    just_nodes.sort()            
    counter = collections.Counter(just_nodes)
    #counter_2 = {k:v/ len(graph) for (k,v) in counter.items()}
    for i in range(1, 21):
        Top = max(counter, key = counter.get)
        print(i)
        print('Node', Top, 'Value' , counter[Top] )
        del counter[Top]


# In[ ]:





# In[4]:


def Dijkstra(graph, start, end = None):
    list1 = list(linkedList)
    #end point - optional, set at None for time analysis to visit all destinations
    n = len(graph)
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
    values = D.values()
    values_list = list(values)
    return values_list


# In[5]:


list1 = list(linkedList)
list2 = []
for i in list1:
    L = Dijkstra(linkedList, i , end = None)
    list2.append(L)


# In[6]:


values_list_2 = []
just_nodes = []
for i in list2:
    for j in i:
        x = 0
        for k in j:
            if x == 0:
                values_list_2.append(k)
                x = x+1
for i in values_list_2:
    for j in i:
        just_nodes.append(int(j))
just_nodes.sort()            
counter = collections.Counter(just_nodes)
#counter_2 = {k:v/ len(just_nodes) for (k,v) in counter.items()}
for i in range(1, 21):
    Top = max(counter, key = counter.get)
    print(i)
    print('Node ID:', Top)
    print('Betweenness Centrality:' , counter[Top] )
    del counter[Top]


# In[ ]:




