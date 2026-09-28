class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #all the opening stuff
        opening=["{","(","["]
        closing =["}",")","]"]
        hashSet ={}
        hashSet["{"]="}"
        hashSet["["]="]"
        hashSet["("]=")"
        for char in s:
            if(char in opening):
                stack.append(char)
            if(char in closing):
                if(len(stack)==0):
                    return False
                popNext = stack.pop()
                if hashSet[popNext]!=char:
                    return False
        if len(stack)==0:
            return True
        return False

 
        