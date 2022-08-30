# https://leetcode.com/problems/search-suggestions-system/

# note: non-optimal solution

from collections import defaultdict
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    prefixes = defaultdict(list)
    for product in products:
        for i in range(1, min(len(product)+1, len(searchWord)+1)):
            key = product[:i]
            prefixes[key].append(product)
    
    ans = []
    max_search_results = 3
    for i in range(1, len(searchWord)+1):
        search = searchWord[:i]
        ans.append(prefixes[search][:max_search_results])
        
    return ans