# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        dequeX=deque([[root, float("-inf"), float("inf")]])
        while len(dequeX)>0:
            thing = dequeX.popleft() 
            node=thing[0]
            left=thing[1]
            right=thing[2]

            if not (node.val>left and node.val<right):
                return False
            if node.left is not None:
                dequeX.append([node.left,left,node.val])
            if node.right is not None:
                dequeX.append([node.right,node.val,right])
        return True

            
            
            


        