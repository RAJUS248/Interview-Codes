arr = [1,2,2,2,3,3,3,3,3,3,3,4,4]

dublicate = []                           # extra memeory/ extra list

for index in range(len(arr) - 1):       # traversing each numbers in an array


    if arr[index] == arr[index + 1]  and arr[index] not in dublicate:  # checking if any dublicate is present and help to avoid the appending same numbers

       
        dublicate.append(arr[index])     # it will store the number in new list/array

print(dublicate)












def dublicate_array(arr):

    # extra memeory/ extra list
    dublicate = []  

    # traversing each numbers in an array                      
    for index in range(len(arr)-1):

        # checking if any dublicate is present and help to avoid the appending same numbers
        if arr[index] == arr[index+1] and arr[index] not in dublicate :
            
            # it will store the number in new list/array
            dublicate.append(arr[index])

    print(dublicate)

sorted_array = [1,2,2,2,3,3,3,3,3,3,3,4,4]

dublicate_array(sorted_array)     # calling the function



