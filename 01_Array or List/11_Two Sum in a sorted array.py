def two_sum(arr,target):

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                
                print(i,j)
         

arr = [1, 2, 3, 4, 6]
target = 6
two_sum(arr,target)