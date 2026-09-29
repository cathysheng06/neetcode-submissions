# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #if its two children find common parent
        #if 1 children, 1 parent of children, that parent counts
        node=root
        while node:
            minNode = min(p.val,q.val)
            maxNode = max(p.val,q.val)
            if node.val>=minNode and node.val<=maxNode:
                return node
            elif minNode>node.val and maxNode>node.val:
                node=node.right
            elif minNode<node.val and maxNode<node.val:
                node=node.left 
        


        