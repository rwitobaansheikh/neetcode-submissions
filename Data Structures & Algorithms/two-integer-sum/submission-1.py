class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash={}
        for i,num in enumerate(nums):
            if target-(target-num) in hash.keys():
                return [hash[target-(target-num)],i]
            else:
                hash[target-num]=i

        