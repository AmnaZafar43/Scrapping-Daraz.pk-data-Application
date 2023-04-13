# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 23:29:34 2022

@author: aa
"""

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])
    
    # Insert elements into their respective buckets
    for j in array:
        index_b = int(len(array) * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
