def secondMax(arr):
    maximum=float('-inf')
    secondMax=float('-inf')

    for item in arr:
        if item>maximum:
            secondMax=maximum
            maximum=item
            
        elif item>secondMax and item<maximum:
            secondMax=item
    return(secondMax)
        




print(secondMax([1,2,37,8,9]))