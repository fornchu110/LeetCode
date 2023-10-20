#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By dfs, time: O(n), space: O(1)
# �D�XBST���Ҧ�node�ۤv��val+�k��tree val����, �]�OBST�ҥH�k�賣�Ovalue��ۤv�j��node
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tmp = 0
        def dfs(node):
            if node is not None:
                # ���i��, �k�䪺node����value���`�ç�s�L, �~���쥪�䪺node
                nonlocal tmp
                dfs(node.right)
                tmp += node.val
                node.val = tmp
                dfs(node.left)
        # �qroot�}�l���X, ��->�k->��
        dfs(root)
        return root
        
# @lc code=end

