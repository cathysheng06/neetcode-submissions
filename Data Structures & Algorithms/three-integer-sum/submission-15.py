class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[]
        for i in range(len(nums)):
            
            leftP=i+1
            rightP=len(nums)-1
            if(nums[i]>0):
                break
            if (nums[i]==nums[i-1] and i>0):
                continue
            while(leftP<rightP):
                sumS = nums[i]+nums[leftP]+nums[rightP]

                if(sumS<0):
                    leftP+=1
                elif (sumS>0):
                    rightP-=1
                else:
                    answer.append([nums[i],nums[leftP],nums[rightP]])
                    leftP+=1
                    rightP-=1
                    while(leftP<rightP and nums[leftP]==nums[leftP-1]):
                         
                        leftP+=1
        return answer
            

  