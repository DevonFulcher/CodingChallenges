# https://www.pramp.com/challenge/L3wQBnQYAEh5K97W9ONK

def get_indices_of_item_wights(arr, limit):
    val_to_i = {}
    for i, val in enumerate(arr):
        curr = limit - val
        if curr in val_to_i:
            return [i, val_to_i[curr]]
        val_to_i[val] = i
    return []
