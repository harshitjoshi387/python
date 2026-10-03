def findMax(arr):
    maximum=arr[0]
    for item in arr:
        if item>maximum:
            maximum=item
        
    return maximum       

print(findMax([1,2,3,4,5]))