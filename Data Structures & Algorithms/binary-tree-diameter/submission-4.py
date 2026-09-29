# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # update the max diameter
            # (left + right) is the diameter through the current node
            res = max(res, left + right)
            
            # return the diameter through the parent node
            # remember diameters means we need the count of edges here
            return 1 + max(left, right)

        dfs(root)

        return res