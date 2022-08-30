from collections import defaultdict
from typing import List

def subdomain_visits(cpdomains: List[str]) -> List[str]:
    counter = defaultdict(int)
    for cpdomain in cpdomains:
        visits, domain = cpdomain.split(" ")
        subdomain = ""
        for domain_part in domain.split(".")[::-1]:
            if subdomain:
                subdomain = domain_part + "." + subdomain
            else:
                subdomain = domain_part
            counter[subdomain] += int(visits)
    ans = []
    for k, v in counter.items():
        ans.append(f"{v} {k}")
    return ans
