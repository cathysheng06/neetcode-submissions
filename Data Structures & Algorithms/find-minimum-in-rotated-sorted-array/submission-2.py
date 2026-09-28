class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        mid = (left+right)//2
        answer = min(nums[left],nums[right])
        while(left<right): 
            
            if(nums[left]<=nums[mid]):
                
                left=mid+1
                answer= min(nums[left],answer)
            else:
                answer=min(nums[mid],answer)
                right=mid-1
            mid = (left+right)//2
        return answer
            

        
        
        