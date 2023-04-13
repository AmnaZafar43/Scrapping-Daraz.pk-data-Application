import math
import random
import time
'''
def RandomArray(size): # to generate random array
    arr = []
    for i in range(size):
        num = random.randint(0,size)
        arr.append(num)
    return arr
'''

def Merge(array,p,q,r): # to merge
    Left = []
    Right = []
    n1 = q-p+1
    n2 = r-q
    for i in range(n1+1):
        Left.append(array[p+i-1])
    for j in range(n2+1):
        Right.append(array[q+j])
    Left.append(10000000)
    Right.append(10000000) 
    i = 1
    j= 1
    for k in range(p,r+1):
        if(Left[i] <= Right[j]):
            array[k] = Left[i]
            i = i+1
        else:
            array[k] = Right[j]
            j= j+1
            
def MergeSort(array,p,r): # to apply merge sort
    if(p<r):
        q = math.floor((p+r)/2)
        MergeSort(array,p,q)
        MergeSort(array,q+1,r)
        Merge(array, p, q, r)

def HybridMergeSort(array,start,end): # hybrid merge 
    if(start<end):
        q = math.floor((start+end)/2)
        MergeSort(array,start,end)
        MergeSort(array,q+1,end)
        Merge(array, start, q, end)
    else:
        for j in range(start,end):
            key = array[j]
            i = j-1
            while(i>=0 and array[i] > key):
                array[i+1] = array[i]
                i=i-1
                array[i+1] = key

arr = []

#Take starting and ending index to apply hybrid merge sort
start = int(input("Enter starting index "))
end = int(input("Enter ending index "))
#calculate starting time
s = time.time()

#call hybrid merge sort function
HybridMergeSort(arr,start,end)

#calculate ending time
e = time.time()

#print(arr[start:end:1]) #only to check the sorted portion
print(arr)
#calculate run time
run = e - s
print("Runtime of hybrid sort in seconds is: ",run)

#to write the sorted portion of array in text file
s = (arr[start:end:1]) 
file = open("SortedHybridSort.csv",mode = "w")
for i in s:
    file.write(str(i)+"\n")
