class Solution:
    def isPalindrome(self, s: str) -> bool:
 
        leftP=0
        rightP=len(s)-1
        while(leftP <rightP): 
            while(leftP<rightP and not s[leftP].isalnum()):
                leftP+=1
            while(leftP<rightP and not s[rightP].isalnum()):
                rightP-=1
            if(s[leftP].lower()!=s[rightP].lower()):
                return False 
            leftP+=1
            rightP-=1
        return True
 
        #if len(s)%2==0:
            #leftP=0
           # rightP=len(s)-1
           # for i in range(len(s)/2):
              #  if(s[leftP]==s[rightP]):


                #leftP+=1
               # rightP-=1
                

        