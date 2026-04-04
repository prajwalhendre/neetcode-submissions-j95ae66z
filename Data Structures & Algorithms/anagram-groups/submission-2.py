from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initialize a dict for every group
        groups = defaultdict(list)
        for s in strs:
            #sorted takes every string, splits the characters and orders them while tuple stores them as a key
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())