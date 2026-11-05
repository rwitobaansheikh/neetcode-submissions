class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i,j=0,len(heights)-1
        maxWater=0
        while i<j:
            maxWater=max((j-i)*min(heights[i],heights[j]),maxWater)
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1

        return maxWater





        