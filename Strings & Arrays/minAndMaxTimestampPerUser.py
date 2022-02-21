"""
Suppose we have an unsorted log file of accesses to web resources.
Each log entry consists of an access time, the ID of the user making the access, and the resource ID. 
The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.
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
    ["54359", "user_1", "resource_3"],
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

def group_by_user(session_list):
    user_to_session = defaultdict(list)
    for time_str, user, resource in session_list:
        time = int(time_str)
        if user_to_session[user]:
            if time < user_to_session[user][0]:
                user_to_session[user][0] = time
            if time > user_to_session[user][1]:
                user_to_session[user][1] = time
        else:
             user_to_session[user] = [time, time]
    return user_to_session