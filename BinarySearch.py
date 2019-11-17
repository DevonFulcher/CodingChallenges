def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left+1 < right:
        mid = (right-left)//2+left
        if targe < arr[mid]:
            right = mid
        else: #arr[mid]>target
            left = mid

    return mid