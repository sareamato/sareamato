#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import queue
import numpy as np


# In[2]:


#If you get an error IOPub data rate exceeded - change data rate allowed


# In[3]:


#merge without adjacency matrix to ensure proper numbering


# In[8]:


def merge(csv1, csv2):
    cols = [0,1,2,3]
    #include coordinates to identify duplicates
    df1 = pd.read_csv(csv1,usecols = cols, header = 0)#import csv
    df2 = pd.read_csv(csv2, usecols = cols, header = 0)
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


    G = df_merged_allcols[['NodeID', 'ConnectedNodeID', 'Distance']]
    print( G)



# In[9]:


merge('Project3_G1_Data.csv', 'Project3_G2_Data.csv')


# In[ ]:


#merge with adjacency matrix representation which ensures G is labeled from 0 to len(G) with consectuive numbers (no gaps from duplicates being deleted)


# In[11]:


def merge_cleanmatrix(csv1, csv2):
    cols = [0,1,2,3]
    #include coordinates to identify duplicates
    df1 = pd.read_csv(csv1,usecols = cols, header = 0)#import csv
    df2 = pd.read_csv(csv2, usecols = cols, header = 0)
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

    # MATRIX CREATION
    #I use the matrix as an intermediate step to ensure the nodes are labeled correctly from 0 to end
    G = (np.ones((n2+4, n2+4), dtype = int))*INF
    dist = (np.ones((n2+4, n2+4), dtype = int))*INF
    for x in range(0, n):
        distance = df_merged_clean.at[int(x), 'Distance']
        row = df_merged_clean.at[int(x), 'NodeID']
        col = df_merged_clean.at[int(x), 'ConnectedNodeID']
        G[row,col] = distance

    #deleting blank duplicate columns
    G = np.delete(G, [2000,1959,1916,1910], axis = 1)

    #deleting duplicate row
    G = np.delete(G, [2000,1959,1916,1910], axis = 0)
    
    #print(G)
        
    
    #G in edge list format
    list1 = []
    for i in range(len(G)):
    #for i in range rows
        for j in range(len(G[0])):
        #for j in range columns
            if G[i,j] != INF:
                list1.append([str(i),str(j), G[i,j]] )
    #print(list1)




# In[12]:


merge_cleanmatrix('Project3_G1_Data.csv', 'Project3_G2_Data.csv')


# In[7]:


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
print( df_merged_clean)

    


# In[ ]:




