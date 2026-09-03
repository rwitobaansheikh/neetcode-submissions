class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length)
            return false;

        let alphabet_count=new Array(26).fill(0);

        for(let i=0;i<s.length;i++){
            alphabet_count[s.charCodeAt(i)-'a'.charCodeAt(0)]+=1;
            alphabet_count[t.charCodeAt(i)-'a'.charCodeAt(0)]-=1;
        }

        for(let i = 0; i<alphabet_count.length; i++){
            if(alphabet_count[i]!=0)
                return false;
        }

        return true;
    }
    
}
