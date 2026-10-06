def max_sum_k(arr,k):
    window_sum=sum(arr[:k])
    best= window_sum

    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k] +arr[i]
        best =max(best,window_sum)
    return best


print(max_sum_k([2,1,5,1,3,2],3))