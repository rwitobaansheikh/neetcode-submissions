class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}

        for i in strs:
            str_idx=[0]*26
            for j in i:
                str_idx[ord(j)-ord('a')]+=1
            str_idx=tuple(str_idx)
            if str_idx not in hash.keys():
                hash[str_idx]=[i]
            else:
                hash[str_idx].append(i)

        return list(hash.values())

        