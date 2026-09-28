class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)<=1):
            return len(s)
        leftP=0
        rightP=1
        seen=set()

        
        maxL=0
        seen.add(s[leftP])
        while(rightP<len(s)):

            if (s[rightP] not in seen):
                seen.add(s[rightP]) 
            else:
                while(s[rightP] in seen):
                    seen.remove(s[leftP])
                    leftP+=1
                seen.add(s[rightP])
            length = rightP-leftP+1
            maxL=max(length,maxL)
            rightP+=1
        return maxL

                


        