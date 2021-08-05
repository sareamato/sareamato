#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np

import pandas as pd
import random as rd


# In[44]:




#Euclidean Distance
def euclidean_distance(list1,list2):
    x = sum([(list1[i]-list2[i])**2 for i in range(len(list1))])
    return x

#find the first cluster assignments:
def cluster_assignment(centroids,df):
    clusters = [[] for i in range(len(centroids))]
    for index, row in df.iterrows():
        distances = [euclidean_distance(row,centroid) for centroid in centroids]
        closest_cluster = np.argmin(distances)
        clusters[closest_cluster].append(row)
    return clusters

#calculate centroids from the means of points in clusters
def reassign(clusters):
    centroids = [sum(cluster)/len(cluster) for cluster in clusters]
    return centroids

def kmeans_tc(k,csv):
    #only for the test case because we don't need the third column
    cols = [0,1]
    df1 = pd.read_csv(csv, usecols= cols)
    centroids = df1.sample(n=k).values.tolist()
    # In order to create the centroids I am selecting a random sample of items from the df axis
    # n = k number of centroids
    clusters = cluster_assignment(centroids,df1)
    nc = reassign(clusters)
    loss = sum([euclidean_distance(centroids[i],nc[i]) for i in range(k)])
    print('Loss:')
    iterations = 1
    while loss > 0:
        #this is the stopping criteria, convergence
        centroids = nc
        clusters = assign_cluster(centroids,df1)
        nc = reassign(clusters)
        loss = sum([euclidean_distance(centroids[i],nc[i]) for i in range(k)])
        print(loss)
        iterations = iterations + 1
    for i in range(k):
        print('Coordinates - Centroid', i+1, ':')
        print(centroids[i])   

    for i in range(0, k):
        print('Number of points in centroid', i+1 , ':')
        print(len(clusters[i]))
    
def kmeans(k,csv):
    losslist = []
    #the only difference is we are using all columns for the power consumption data set  
    df1 = pd.read_csv(csv)
       #only for the test case because we don't need the third column
    centroids = df1.sample(n=k).values.tolist()
    # In order to create the centroids I am selecting a random sample of items from the df axis
    # n = k number of centroids
    clusters = cluster_assignment(centroids,df1)
    nc = reassign(clusters)
    loss = sum([euclidean_distance(centroids[i],nc[i]) for i in range(k)])
    print('Loss:')
    iterations = 1
    while loss > 0 and iterations < 15:
        #this is the stopping criteria, convergence
        centroids = nc
        clusters = assign_cluster(centroids,df1)
        nc = reassign(clusters)
        loss = sum([euclidean_distance(centroids[i],nc[i]) for i in range(k)])
        losslist.append(loss)
        iterations = iterations + 1
        if k == 2:
            print(loss)
        else:
    
            scatter_point = losslist[-1]
            print(scatter_point)
        
    
    for i in range(k):
        print('Coordinates - Centroid', i+1, ':')
        print(centroids[i])   

    for i in range(0, k):
        print('Number of points in centroid', i+1 , ':')
        print(len(clusters[i]))
    
 
 


# In[ ]:


kmeans_tc(2,'Project3_Test_Case.csv')


# In[45]:


kmeans(2,'Project3_Power_Consumption.csv')


# In[7]:


for k in range(3,21):
    print('k = ' , k)
    kmeans(k,'Project3_Power_Consumption.csv')


# In[ ]:




