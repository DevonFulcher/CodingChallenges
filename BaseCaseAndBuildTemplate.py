'''
best for finding permutations and combinations

def top_down(source, pointer, current_combination)
  if is_final_combination(current_combination):
    # print the current combination # OR add combination to result array
    (print current_combination) OR result.append(current_combination)
  else:
    # get_next_elem changes depending on the problem
    next_elem_to_add = get_next_elem(source, pointer)
    top_down(source, pointer + 1, current_combination + next_elem_to_add)
'''