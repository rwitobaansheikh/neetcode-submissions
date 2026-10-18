class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        appearance=set()
        for i in nums:
            if i not in appearance:
                appearance.add(i)
            else:
                return True

        return False
