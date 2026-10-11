# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)





#        0 1 2 3 4 5
# ino -> 5 2 6 1 3 4
#        l   r   l r
#        lr
# pre -> 1 2 5 6 3 4
#          i