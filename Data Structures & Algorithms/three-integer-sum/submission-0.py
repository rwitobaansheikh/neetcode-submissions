class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result=[]
        nums.sort()
        for i, val in enumerate(nums):
            if i!=0 and val==nums[i-1]:
                continue
            
            j,k=i+1,len(nums)-1

            while j<k:
                threeSum=val+nums[j]+nums[k]

                if threeSum<0:
                    j+=1
                elif threeSum>0:
                    k-=1
                else:
                    result.append([val,nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1


        return result

            



        