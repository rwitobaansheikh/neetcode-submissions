class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash={}

        for i,j in enumerate(numbers):
            diff=target-j
            if j not in hash.keys():
                hash[diff]=i+1
            else:
                return [hash[j],i+1]

        pass

        