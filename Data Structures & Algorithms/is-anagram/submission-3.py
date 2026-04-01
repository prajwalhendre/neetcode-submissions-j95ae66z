class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1
        
        for letter in t:
            seen[letter] = seen.get(letter, 0) -1
        
        return all(v == 0 for v in seen.values())