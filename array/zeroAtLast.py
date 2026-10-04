def number(number):
    arr1=[]
    count=0
    for item in number:
        if item!=0:
            arr1.append(item)
        else: count=count+1
    arr1 = arr1 + [0] * count
    return arr1

print(number([0,-3,5]))