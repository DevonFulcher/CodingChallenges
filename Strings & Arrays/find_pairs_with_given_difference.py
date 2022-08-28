# https://www.pramp.com/challenge/XdMZJgZoAnFXqwjJwnpZ

def find_pairs_with_given_difference(arr, k):
    num_set = set(arr)
    ans = []
    for val in arr:
        if k + val in num_set:
            ans.append([k+val, val])
    return ans
