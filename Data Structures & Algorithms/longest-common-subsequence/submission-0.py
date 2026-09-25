class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
 
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if(text1[i]==text2[j]):
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]


 
#
#class Solution:
    #def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
       # def dfs(index1, index2):
          #  if index1>=len(text1) or index2>=len(text2):
               # return 0
            #if text1[index1]==text2[index2]:
               # dfs(index1+1,index2+1)
           # return max(dfs(index1+1,index2), dfs(index1,index2+1))
        #dfs(0,0)

        
