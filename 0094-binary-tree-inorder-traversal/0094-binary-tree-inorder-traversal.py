# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.li = []
        self.helper(root)
        return self.li

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.li.append(root.val)
            self.helper(root.right)

        