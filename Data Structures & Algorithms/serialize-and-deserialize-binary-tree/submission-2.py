# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []

        def dfs(node):
            if not node:
                serial.append("N")
                return

            serial.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(serial)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if data[i] == "N":
                i += 1
                return None
            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
