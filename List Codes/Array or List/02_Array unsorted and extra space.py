arr = [-1,-1,2,2,3]

new_list = []               # storing arr
dublicate = []              # dublicate arr storing

for num in arr:             # number in array list
    if num in new_list:                 # if number pressnt il new_list then it goes 
        if num not in dublicate:        # and check in dublicate then it not in dublicate
            dublicate.append(num)       # it will append to dublicate

    else:                              # numbefr not in new_list
        new_list.append(num)           # it will append number in new_list

print(arr)
print(dublicate)                       # print the dublicate

num = [1,2]
arr = [1]
for num2 in num:
    if num2 not in arr:
        
        print(num2)








"""
# using set o(n) time complexity    Chatgpt

def dublicates(arr):

    new_set = set()         # for storing the num in set
    dublicate = set()       # only stores dublicates without repeating

    for num in arr:
        if num in new_set:      # check and add the number to the set
            dublicate.add(num)      # if num in set then it will add to dublicate

        else:
            new_set.add(num)        #  if num is not in set it will add to new_set

    return list(dublicate)          # return and convert the set into list

arr = [1,3,4,5,1,2,4,3,4,1,2,7,8,9]
print(dublicates(arr))    """











