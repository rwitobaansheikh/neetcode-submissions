class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for str in strs:
            string_ct=[0]*26
            for ch in str:
                string_ct[ord(ch)-ord('a')]+=1

            key=tuple(string_ct)

            if key not in hash.keys():
                hash[key]=[str]
            else:
                hash[key].append(str)
                
        return list(hash.values())

        