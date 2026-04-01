# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case of both trees empty 
        if not p and not q:
            return True
        #base care of one tree emtpy
        if not p or not q:
            return False
        #one val doesn't match the others
        if p.val != q.val:
            return False
        
        #run it on the left and right nodes
        return (self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))