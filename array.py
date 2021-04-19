def sum(arr):

    sum=0
    for i in arr:
        sum+=i
        print(sum)
    return(sum)
arr=[]
arr=[1,3,2]

answer=sum(arr)
print("answer is" + str(answer))