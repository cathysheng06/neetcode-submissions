class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left =0
        right =len(nums)-1
        mid = (left+right)//2 
        while(left<=right):
            if(nums[mid]==target):
                return mid
            if (nums[left]<=nums[mid]):
                if(target<nums[left] or target>nums[mid]):
                    left=mid+1
                else:
                    right=mid-1
            else:
                if(target>nums[right] or target<nums[mid]):
                    right=mid-1
                else:
                    left=mid+1 
            mid=(left+right)//2
        return -1
                    

            
        