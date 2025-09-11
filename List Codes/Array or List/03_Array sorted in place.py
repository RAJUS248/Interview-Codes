
def dublicates(arr):

    for index in range(len(arr)-1):         # traversing each numbers in an array

        if arr[index] == arr[index + 1]:    # checking the 1st element and next element

            if index == 0 or arr[index] != arr[index - 1]:  # if arr as 1 element or present and preveous are equal or not
                                                            # if equals it skips if not then it print the dublicate 
                print(arr[index], end = " ")

arr = [1,2,2,3,3,3,3,5,5,5,5,5,6,7]
dublicates(arr)