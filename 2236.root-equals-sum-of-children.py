<<<<<<< HEAD
#
# @lc app=leetcode id=2236 lang=python3
#
# [2236] Root Equals Sum of Children
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By node, time: O(1), space: O(1)
# �N�O�n���Droot��val�O�_����child��val�`�M
# �����breturn�P�_�N�n
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val==root.left.val+root.right.val

# @lc code=end

=======
#
# @lc app=leetcode id=2236 lang=python3
#
# [2236] Root Equals Sum of Children
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By node, time: O(1), space: O(1)
# �N�O�n���Droot��val�O�_����child��val�`�M
# �����breturn�P�_�N�n
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val==root.left.val+root.right.val

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
