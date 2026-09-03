class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen= new Map();
        for(let i=0;i<nums.length;i++){
            const diff=target-nums[i];
            if(seen.has(target-diff)){
                return [seen.get(target-diff),i]
            }
            else
                seen.set(diff,i);
        }
    }
}
