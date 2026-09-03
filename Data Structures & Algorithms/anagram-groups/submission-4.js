class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hash = new Map();
        for(const str of strs){
            const count_alpha=new Array(26).fill(0);

            for(const ch of str){
                count_alpha[ch.charCodeAt(0)-'a'.charCodeAt(0)]+=1;
            }

            const key=count_alpha.join(',');

            if(!hash.has(key))
                hash.set(key,[]);

            hash.get(key).push(str);

        }
        return Array.from(hash.values());
    }
}
