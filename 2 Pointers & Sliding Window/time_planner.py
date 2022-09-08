# https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5Lg1

def meeting_planner(slotsA, slotsB, dur):
  a_ptr, b_ptr = 0, 0
  
  while a_ptr < len(slotsA) and b_ptr < len(slotsB):
    greater_start_time = max(slotsA[a_ptr][0], slotsB[b_ptr][0])
    lesser_end_time = min(slotsA[a_ptr][1], slotsB[b_ptr][1])
    if lesser_end_time - greater_start_time >= dur:
      return [greater_start_time, greater_start_time+dur]
    
    if slotsA[a_ptr][1] < slotsB[b_ptr][1]:
      a_ptr += 1
    else:
      b_ptr += 1
  return []