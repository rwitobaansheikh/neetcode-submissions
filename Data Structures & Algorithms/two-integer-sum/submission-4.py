class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,j in enumerate(nums):
            diff=target-j
            if j not in hash.keys():
                hash[diff]=i
            else:
                return [hash[j],i]

        pass
            

        