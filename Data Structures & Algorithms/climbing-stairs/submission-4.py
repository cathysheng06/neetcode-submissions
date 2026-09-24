class Solution:
    def climbStairs(self, n: int) -> int:
        box = [1,2]
        if n<=2:
            return box[n-1]
        for i in range((n-2)):
            temp=box[0]
            box[0]=box[1]
            box[1]=temp+box[1]
        return box[1]
        