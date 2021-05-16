def leftshift(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[1,2,3,4,5]
print(arr)
print(leftshift(arr,2,len(arr)))

