from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            split = email.split("@")
            local_name = split[0]
            domain_name = split[1]
            normalized = "".join(list(filter(lambda char: char != ".", local_name)))
            i = 0
            while i < len(normalized):
                if normalized[i] == "+":
                    break
                i += 1
            if i < len(normalized):
                normalized = normalized[:i]
            email_set.add(normalized + "@" + domain_name)
        return len(email_set)