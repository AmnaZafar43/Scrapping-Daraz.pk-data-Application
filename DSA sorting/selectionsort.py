# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:36:01 2022

@author: aa
"""

def Minimum(Arr,starting,ending):
    minimum=Arr[starting]
    minimumidx=starting
    for x in range(starting,ending+1):
      if(Arr[x]<minimum):
          minimum=Arr[x]
          minimumidx=x
    return minimumidx

def SelectionSort(array,start,end):
    minimum=0
    for i in range(start,end+1):
        minimum=Minimum(array,i,end)
        temp=array[i]
        array[i]=array[minimum]
        array[minimum]=temp
    return array