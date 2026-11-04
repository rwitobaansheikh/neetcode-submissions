class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for ch in (s):
            if ch.isalnum(): 
                new_s+=ch.lower()

        for i in range(len(new_s)):
            k=-i-1
            if new_s[i] != new_s[k]:
                return False

        return True


        