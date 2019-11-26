'''
start: 11:16am
X loop through array 1, loop through array 2, if array array if element of array 2 is matched in array 1 append it to result(cant append it is a tuple)

X dictionary solution

two pointers solution:
    loop while pointers are in range of len. i.e. while indexa < len(a)
    start pointers at the front of each list, if value equals then append and increment both, if val 1 < val 2 then incrment val 1 dont append, same with val 2
    work around tuple immutability with lists?

[1,3,6,17,21],  -> (6, 21)
          ^              
[2,4,6,21]
       ^

[1, 5]
    ^
[3, 4]
    ^

[0, 1, 3, 3, 3, 4] -> (3, 3)
                ^
[2, 3, 3, 5]
          ^

[], [] -> ()
[], [1] -> (1)
[1,2,3], [2,3] -> (2, 3)

start coding: 11:26am
complete: 11:46am
'''

def intersection_of_arrays(arr1, arr2):
    pointer1 = 0
    pointer2 = 0
    resultList = [] # lists are mutable unlike tuples. we will copy this in to a tuple later
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] == arr2[pointer2]:
            resultList.append(arr1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif arr1[pointer1] < arr2[pointer2]:
            pointer1 += 1
        else: # arr1[pointer1] > arr2[pointer2]
            pointer2 += 1
    return tuple(resultList)