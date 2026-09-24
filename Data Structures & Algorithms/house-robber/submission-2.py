class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 =0
        rob2=0
        for n in nums:
            temp=max(rob1+n,rob2)
            rob1=rob2
            rob2=temp  
        return rob2
        


###
#class Solution:
 #   def rob(self, nums:List[int])->int:
  #      arr=[nums[0],nums[1],nums[2]]
      #  for i in range(len(nums)-2):



###
#class Solution:
   # def rob(self, nums:List[int])->int:
    #    dfsArr={}
     #   def dfs(index):
      #      
        #    if index>=len(nums):
       #         return 0  
         #   if index in dfsArr:
          #      return dfsArr[index] 
            #dfsArr[index]=max(nums[index]+dfs(index+2), dfs(index+1))
          #  return dfsArr[index]
       # dfs(0)
      #  for i in range(len(nums)):
            #return max(nums[i]+dfs(i+2),dfs[i+1])

####
#class Solution:
 #   def rob(self,nums:List[int])->int: 
        #def func(subArr, maxX):
            #for i in range(arr): 
               # answer=subArr[i] 
               # if i-1>=0:
               #     answer+=func(subArr[:i-1],maxX)
               # if i+1<=len(arr)-1:
                #    answer+=func(subArr[i+1:],maxX)
               # if answer>maxX:
                 #   maxX=answer
            #return maxX
        #return func(nums, -1)
       # return maxX