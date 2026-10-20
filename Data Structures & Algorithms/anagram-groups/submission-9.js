class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let hash = new Map();

        for(const str of strs){
            let str_idx=new Array(26).fill(0);
            for(const ch of str){
                str_idx[ch.charCodeAt(0)-'a'.charCodeAt(0)]+=1;
            }
            const key=str_idx.toString();
            if(hash.has(key)){
                hash.get(key).push(str);
            }
            else
                hash.set(key,[str]);
        }

        return Array.from(hash.values())
    }
}
