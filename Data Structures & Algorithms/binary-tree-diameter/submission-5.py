# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node and node.left not in mp:
                stack.append(node.left)
            elif node and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                lH, lD = mp[node.left]
                rH, rD = mp[node.right]
                mp[node] = (1 + max(lH, rH), max(lH + rH, lD, rD))

        return mp[root][1]