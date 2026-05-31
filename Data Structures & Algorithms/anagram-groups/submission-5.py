class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for string in strs:
            default = sorted(string)
            default = tuple(default)
            if default in groups:
                groups[default].append(string)
            else:
                groups[default] = []
                groups[default].append(string)
        res = []
        for group in groups.values():
            res.append(group)
        return res
