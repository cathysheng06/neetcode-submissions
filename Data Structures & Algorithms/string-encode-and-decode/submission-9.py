class Solution: 
    def encode(self, strs: List[str]) -> str:
        #i insert the digit length before each string and so i know how much to count forward for each separate string when separating it
        answer=""
        for strX in strs:
            answer+=str(len(strX))+"#"+strX
        return answer

    def decode(self, s: str) -> List[str]:
        answer=[]
        i=0
        while i <len(s):
            
            if s[i].isdigit(): 
                length=""
                while s[i].isdigit() and s[i]!="#":
                    length+=s[i]
                    i+=1
                i+=1 #to skip the #
                strDecode=""
                for j in range(0,int(length)): 
                    strDecode+=s[i+j] 
                answer.append(strDecode)
            i+=int(length)
        return answer
                    


