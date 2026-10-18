class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashs={}
        for i in s:
            if i not in hashs.keys():
                hashs[i]=0
            else:
                hashs[i]+=1
        
        hasht={}
        for i in t:
            if i not in hasht.keys():
                hasht[i]=0
            else:
                hasht[i]+=1

        if hashs==hasht:
            return True

        else:
            return False