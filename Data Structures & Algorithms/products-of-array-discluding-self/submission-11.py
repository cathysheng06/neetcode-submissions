class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #sort it first
        # then have another array that tracks the multiplicatin?
        
        #2*4*6, 1*4*6, 1*2*6, 1*2*4
        prefix=[0]*len(nums)
        prefix[0]=nums[0] 
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i]

        suffix=[0]*len(nums) #starting from the end
        suffix[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]

        answer=[0]*len(nums)
        for i in range(0,len(nums)):
            thing1=1
            thing2=1
            if(i-1>=0):
                thing1=prefix[i-1]
            if(i+1<=len(nums)-1):
                thing2=suffix[i+1]
            answer[i]=thing1*thing2
        return answer

