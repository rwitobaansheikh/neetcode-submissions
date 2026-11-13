class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        for r,char in enumerate(s2):
            if r-l+1 < len(s1):
                continue
            
            if r-l+1==len(s1) and sorted(s1)==sorted(s2[l:r+1]):
                return True
            else:
                l+=1

        return False
        