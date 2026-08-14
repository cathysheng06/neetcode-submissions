class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer=[]
        visited=[0]*len(strs)
        for m in range(0,len(strs)):
            if visited[m]==0:
                x = strs[m]
                arr1= [0]*26
                visited[m]=1
                for i in x:
                        arr1[ord(i)-ord('a')]+=1
                    
                answerSub=[x]
                for n in range(m+1,len(strs)):
                    if visited[n]==0:
                        y = strs[n]
                        arr2= [0]*26
                        for i in y:
                            arr2[ord(i)-ord('a')]+=1
                        if arr1==arr2:
                            answerSub.append(y)
                            visited[n]=1
                answer.append(answerSub)
        return answer
            


        