class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string+=str(len(s))+'#'+s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        k=0
        i=0
        while i < len(s):
            if s[i]=='#':
                str_len=int(s[k:i])
                decoded_strs.append(s[i+1:i+1+str_len])
                k=i+1+str_len
                i=k
            i+=1


        return decoded_strs
                    
