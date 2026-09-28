class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftP=0
        rightP=len(heights)-1
        maxA=-1
        while(leftP<rightP):
            area=(rightP-leftP)*min(heights[leftP], heights[rightP])
            if(heights[leftP]<=heights[rightP]):
                leftP+=1
            elif(heights[rightP]<=heights[leftP]):
                rightP-=1
            if area>maxA:
                maxA=area
        return maxA


'''
        leftP=0
        rightP=len(heights)-1
        maxA=-1 
        while(leftP<rightP):
            area = (rightP-leftP)*min(heights[leftP], heights[rightP])
            prevL=leftP
            prevR = rightP 
            if(heights[leftP]<heights[rightP]):
                while(heights[leftP]<heights[prevL] and leftP<rightP): 
                    leftP+=1
                prevL=leftP
            if(heights[rightP]<heights[leftP]):
                while(heights[rightP]<heights[prevR] and leftP<rightP):
                    rightP-=1 
                prevR = rightP
            if(heights[rightP]==heights[leftP]):
                while(heights[rightP]<heights[prevR] and heights[leftP]<heights[prevL] and leftP<rightP):
                    leftP+=1
                    rightP-=1
                prevL=leftP
                prevR=rightP
            if(area>maxA):
                maxA=area
        return maxA
'''
        

                
