# Binary Search Algorithm
def binarySearch(arr, value):
    lo = 0
    hi = len(arr) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if arr[mid] < value:
            lo = mid + 1
        else:
            hi = mid
    if arr[lo] == value:
        print("Found At Index", lo)
    elif arr[hi] == value:
        print("Found At Index", hi)
    else:
        print("Not Found")

arr = [1, 3, 4, 5, 6]
value = int(input("Enter value you want to search "))
binarySearch(arr,value)

# Searching Algorithm
def search(arr,x):
    for i in range(0, len(arr)):
        if (arr[i] == x):
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = int(input("Enter which element you want to search "))
result = search(arr,x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
