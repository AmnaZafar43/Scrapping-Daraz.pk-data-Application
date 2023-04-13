# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:40:32 2022

@author: aa
"""

def Merge(array,p,q,r):
    count1=q-p+1
    count2=r-q
    C1=0
    C2=0
    Arr1=[]
    Arr2=[]
    while C1<count1:
        Arr1.append(array[C1+p])
        C1=C1+1
    while C2<count2:
         Arr2.append(array[C2+q+1])
         C2=C2+1
    c1=0
    c2=0
    starting = p
    while(c1<count1 and c2<count2):
        if(Arr1[c1]<=Arr2[c2]):
            array[starting]=Arr1[c1]
            c1=c1+1
        else:
             array[starting]=Arr2[c2]
             c2=c2+1
        starting = starting+1
            
    while c1<count1 :
        array[starting]=Arr1[c1]
        c1=c1+1
        starting = starting+1
    while c2<count2 :
        array[starting]=Arr2[c2]
        c2=c2+1
        starting = starting+1
    
def MergeSort(array,start, end):
       
        if start<end:
            q = start+(end-start)//2
            MergeSort(array, start, q)
            MergeSort(array, q+1, end)
            Merge(array,start,q,end)     
        else:
            return      
