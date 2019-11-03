from random import randint

'''
Find the kth largest element in an array. Do it as fast as you can.

Example:

def kth_largest(arr, k):
    pass

kth_largest([1094, 19, 33, 33, 2, -1], 1) # 1093
kth_largest([32,32,32,32], 1) # 32
kth_largest([1,2,3,4,5,6], 1) # 6
kth_largest([6,5,4,3,2,1], 1) # 6
kth_largest([1,2,3,4,5,6], 2) # 5
kth_largest([1,2,3,4,5], 1) # 5
kth_largest([1,2,3,4,5], 2) # 4
kth_largest([1], 1) # 1
'''

# Brute force
def kth_largest(arr, k):
    arr.sort() # n log (N)
    return arr[len(arr)-k]

# print(kth_largest([1094, 19, 33, 33, 2, -1], 1))  # 1094
# print(kth_largest([32,32,32,32], 1))  # 32
# print(kth_largest([1,2,3,4,5,6], 1)) # 6
# print(kth_largest([6,5,4,3,2,1], 1)) # 6
# print(kth_largest([1,2,3,4,5,6], 2)) # 5
# print(kth_largest([1,2,3,4,5], 1))  # 5
# print(kth_largest([1,2,3,4,5], 2))  # 4
# print(kth_largest([1], 1)) # 1

def partition(arr, start, end, pivot_index):
    arr[end],arr[pivot_index] = arr[pivot_index],arr[end]
    pivot = arr[end]
    i = j = start
    while i < end:
        if arr[i] <= pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        i+=1

    arr[j],arr[end]=arr[end],arr[j]
    print('\t' + ''.join([('  {} '.format(x) if x != arr[j] else '|{}| '.format(x)) for x in arr]).strip())
    print()
    return j

def quick_select(arr, k, start, end):
    if start > end:
        return

    pivot = randint(start, end)
    print('Pivot is: {}'.format(arr[pivot]))
    print('Arr is: ' + ' '.join(str(item) for item in arr))
    pivot_index = partition(arr, start, end, pivot)
    if pivot_index==len(arr)-k:
        return arr[pivot_index]
    elif pivot_index < len(arr)-k:
        return quick_select(arr, k, pivot_index+1, end)
    else:
        return quick_select(arr, k, start, pivot_index-1)

def kth_largest(arr, k):
    return quick_select(arr, k, 0, len(arr)-1)

print(kth_largest([1094, 19, 33, 33, 2, -1], 1)) # 1094
# print(kth_largest([32,32,32,32], 1)) # 32
# print(kth_largest([1,2,3,4,5,6], 1)) # 6
# print(kth_largest([6,5,4,3,2,1], 1)) # 6
# print(kth_largest([1,2,3,4,5,6], 2)) # 5
# print(kth_largest([1,2,3,4,5], 1)) # 5
# print(kth_largest([1,2,3,4,5], 2)) # 4
# print(kth_largest([1], 1)) # 1
