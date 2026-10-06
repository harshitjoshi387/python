def missingNum(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return i

print(missingNum([1, 2, 3, 4], [1, 2, 3]))    