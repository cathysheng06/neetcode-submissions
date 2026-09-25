class Solution:
    #can't use the s[i]==s[i+1] check because what about aaa?, for every i check odd and even
    def longestPalindrome(self, s: str) -> str:  
        maxLength =-1
        maxString=""
        for i in range(len(s)): 

            #for even
            leftP=i
            rightP=i+1
            length=2
            substr=""
            while (rightP<len(s) and leftP>=0 and s[leftP]==s[rightP]):
                substr= s[leftP:rightP+1]
                length+=2
                rightP+=1
                leftP-=1
            if length>maxLength:
                maxLength = length
                maxString = substr

            #for odd
            leftP=i
            rightP=i
            length=1
            substr=""
            while (rightP<len(s) and leftP>=0 and s[leftP]==s[rightP]):
                substr= s[leftP:rightP+1]
                length+=2
                rightP+=1
                leftP-=1 
            if length>maxLength:
                maxLength = length
                maxString = substr
                
        return maxString


               # while(s[leftP]==s[rightP] and rightP<=len(s)-2 and leftP>=1):
                  #  length+=1
                  #  rightP+=1
                  #  leftP-=1
                  #  substr=s[leftP]+substr+s[rightP]
