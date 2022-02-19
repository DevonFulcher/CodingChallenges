"""
Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.

Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3)
Reason: resource_3 is accessed at 53760, 54001, and 54060

most_requested_resource(logs2) # => ('resource_3', 4)
Reason: resource_3 is accessed at 1199, 1200, 1201, and 1202

most_requested_resource(logs3) # => ('resource_5', 1)
Reason: resource_5 is accessed at 300
"""


from collections import defaultdict

logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],  
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    [ "54359", "user_1", "resource_3"],
]

logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]

logs3 = [
    ["300", "user_10", "resource_5"]
]

def get_largest_window(resource_timestamps):
    l, r = 0, 0
    window_length = 5*60
    largest_window = 0
    while r < len(resource_timestamps):
        while int(resource_timestamps[r]) - int(resource_timestamps[l]) <= window_length:
            r += 1
            if r >= len(resource_timestamps):
                return max(largest_window, r-l)
        largest_window = max(largest_window, r-l)
        l += 1
    return largest_window

def most_requested_resource(session_list):
    resource_to_timestamp = defaultdict(list)
    for time_str, user, resource in session_list:
        resource_to_timestamp[resource].append(int(time_str))
    
    for resource, value in resource_to_timestamp.items():
        resource_to_timestamp[resource] = sorted(value)
        
    resource_to_request_amount = {}
    
    for resource, value in resource_to_timestamp.items():
        resource_to_request_amount[resource] = get_largest_window(value)

    max_requests = 0
    max_resource = ""
    for resource, requests in resource_to_request_amount.items():
        if requests >= max_requests:
            max_resource = resource
            max_requests = requests
            
    return (max_resource, max_requests)
        
print(most_requested_resource(logs1))
print(most_requested_resource(logs2))
print(most_requested_resource(logs3))