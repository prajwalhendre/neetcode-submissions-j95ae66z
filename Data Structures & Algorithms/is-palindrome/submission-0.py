class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(char.lower() for char in s if char.isalnum())
        t = len(filtered)
        for i in range(len(filtered)):
            if filtered[i] != filtered[t-1]:
                return False
            i += 1
            t -=1
        return True