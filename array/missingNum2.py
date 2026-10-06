def missingNum(arr,n):
    total =n*(n+1)//2
    return total-sum(arr)



print(missingNum([1,2,4,5],5))