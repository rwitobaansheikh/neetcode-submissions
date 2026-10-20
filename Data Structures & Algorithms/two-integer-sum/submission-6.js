class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hash = new Map();

        for(let i=0; i<nums.length;i++){
            let diff=target-nums[i];
            if(hash.has(nums[i])){
                return [hash.get(nums[i]),i];
            }
            else
                hash.set(diff,i);
        }
        return
    }
}
