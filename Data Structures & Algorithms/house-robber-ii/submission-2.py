class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        funcArray=[0,0]
        answer=0 
        for i in range(len(nums)-2,-1,-1): 
            answer=max(nums[i]+funcArray[1],funcArray[0]) 
            temp=funcArray[0]
            funcArray[0]=answer
            funcArray[1]=temp
        compare1=funcArray[0]

        funcArray=[0,0]
        answer=0 
        for i in range(len(nums)-1,0,-1): 
            answer=max(nums[i]+funcArray[1],funcArray[0]) 
            temp=funcArray[0]
            funcArray[0]=answer
            funcArray[1]=temp
        compare2 = funcArray[0]

        return max(compare1, compare2)
        

#
#class Solution:
    #def rob(self, nums: List[int]) -> int:
      #  funcArray=[0,0]
      #  answer=0
      #  for i in range(len(nums)-1,-1,-1):
         #   answer=max(nums[i]+funcArr[1], funcArr[0])
         #   temp=funcArr[0]
          #  funcArr[0]=answer
          #  funcArr[1]=temp
       # return funcArr[0]
            
