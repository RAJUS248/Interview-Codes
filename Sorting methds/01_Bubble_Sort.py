def buuble_sort(arr):

    for i in range(len(arr) -1):
        swapped = False

        for j in range(len(arr)-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if not swapped:
            break
    return arr
arr = [9,4,3,6,7,1,2]
print(buuble_sort(arr))