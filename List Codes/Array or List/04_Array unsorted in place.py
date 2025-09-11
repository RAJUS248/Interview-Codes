def dublicates(arr):
    arr.sort()                              # unsorted arr to sorted arr
    for index in range(len(arr)-1):         # traversing each numbers in an array

        if arr[index] == arr[index + 1]:    # checking the 1st element and next element

            if index == 0 or arr[index] != arr[index - 1]:  # if arr as 1 element or present and preveous are equal or not
                                                            # if equals it skips if not then it print the dublicate 
                print(arr[index], end = " ")

arr = [1,3,4,5,1,2,4,3,4,1,2,7,8,9]
dublicates(arr)