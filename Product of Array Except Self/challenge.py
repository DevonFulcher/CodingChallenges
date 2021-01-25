# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums: list[int]) -> list[int]:
    curr_product = 1
    products_one = []
    for num in nums:
        products_one.append(curr_product)
        curr_product *= num

    curr_product = 1
    products_two = []
    for num in nums[::-1]:
        products_two.append(curr_product)
        curr_product *= num

    result = []
    for nums in zip(products_one, products_two[::-1]):
        result.append(nums[0] * nums[1])

    return result


productExceptSelf([1, 2, 3, 4])
