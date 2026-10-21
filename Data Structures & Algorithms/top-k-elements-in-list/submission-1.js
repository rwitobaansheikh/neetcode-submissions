class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let count = new Map();
        let freq = Array.from({ length: nums.length + 1 }, () => []);

        for(const num of nums){
            count.set(num, (count.get(num)||0)+1);
        }
        for(let[n,c] of count){
            freq[c].push(n);
        }

        let res=[]
        for(let i = freq.length-1; i>=0; i--){
            for(const c of freq[i]){
                res.push(c);
                if(res.length==k)
                    return res
            }
        }
        return res
    }
}
