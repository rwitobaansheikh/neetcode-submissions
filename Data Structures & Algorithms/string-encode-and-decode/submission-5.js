class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded_string="";
        for(const s of strs){
            encoded_string+=s.length+'#'+s;
        }

        return encoded_string;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let decoded_strs=new Array(0);
        let i=0;
        let j=0;
        while(i<str.length){
            if(str[i]==='#'){
                const str_len=parseInt(str.slice(j,i),10);
                decoded_strs.push(str.slice(i+1,i+1+str_len));
                j=i+1+str_len;
                i=j;
            }
            i++;
        }
        return decoded_strs;
    }
}
