class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for letter in s:
            if letter.isalnum():
                res.append(letter.lower())
        l = 0
        r = len(res)-1
        while l <=r:
            if not res[l] == res[r]:
                return False
            l += 1
            r -=1
        return True