def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left+1 < right:
        mid = (right-left)//2+left
        if target < arr[mid]:
            right = mid
        else:  # arr[mid]>target
            left = mid

    if arr[left] == target:
        return left
    return right
