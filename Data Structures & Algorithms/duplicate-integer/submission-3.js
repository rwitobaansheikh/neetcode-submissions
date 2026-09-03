class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen=new Array(0)

        for(let i=0;i<nums.length; i++){
            if(seen.includes(nums[i]))
                return true;
            else
                seen.push(nums[i]);
        }
        return false;
    }
}
