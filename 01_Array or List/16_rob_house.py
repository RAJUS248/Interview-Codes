def rob_house_v2(arr):
    prev1 = 0
    prev2 = 0

    for num in arr:
        temp = prev1
        prev1 = max(prev2 + num ,prev1)
        prev2 = temp

    return prev1

arr = [6, 7, 1, 30, 8, 2, 4]
print(rob_house_v2(arr))
