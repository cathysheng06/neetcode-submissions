# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        node=root

        answer=[]
        answer.append([root.val])
        dequeX=deque([root]) 
        row=[]
        while len(dequeX)>0:
            row =[]
            newDeque=deque()
            for i in range(0, len(dequeX)):
                node=dequeX.popleft()
                if(node.left is not None):
                    row.append(node.left.val)
                    newDeque.append(node.left)
                if(node.right is not None): 
                    row.append(node.right.val)
                    newDeque.append(node.right)
            dequeX=newDeque
            if row!=[]:
                answer.append(row)

        return answer

        