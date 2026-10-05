def freqOfNum(arr):
    count={}

    for ch in arr:
        if ch in count:
            count[ch]=count[ch]+1
        else: count[ch]=1

    return(count)

print (freqOfNum("Harshitjoshi"))