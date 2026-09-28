class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashS={}
        for i in range(len(nums)):
            if nums[i] in hashS:
                return [hashS[nums[i]],i]
            hashS[target-nums[i]]=i #the index
            
        