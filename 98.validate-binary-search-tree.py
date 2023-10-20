#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# ��tree�P�_�O�_��BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n)
# �`�NBST�ʽ�, ��sub tree�@�w��root�p, �ksubtree�@�w��root�j
# float("-inf")�N��t�L�a�j, float("inf")�N���L�a�j
# �]�p���helper�ɴN�n���w�q�n�̤j�d��
class Solution:
    def helper(self, node, lower = float('-inf'), upper = float('inf')) -> bool:
        if not node:
            return True
        val = node.val
        # �N��root���b(lower, upper)��
        if val<=lower or val>=upper:
            return False
        # ��sub tree�Ҧ�node.val�u��b(lower, val)���~�OBST
        if not self.helper(node.left, lower, val):
            return False
        # �ksub tree�Ҧ�node.val�u��b(val, upper)���~�OBST
        if not self.helper(node.right, val, upper):
            return False
        # �N��sub tree�M�ksub tree�Ҧ�node.val�T�곣�b�d��
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        # �I�shelper�æ^�ǵ��G, �u���Ѽ�root�N���Χ�slower�Mupper
        return self.helper(root)
    
# By inorder traversal, time: O(n), space: O(n)
# �[��inorder traversal BST
# �o�{���X�쪺node.val���_�W�ɨ쨫�X�����N�N��OBST, �Ϥ��DBST
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         stack, inorder = [], float('-inf')
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             # �p�G���X�쪺�snode.val�p��W�@��node.val, �N���OBST
#             if root.val <= inorder:
#                 return False
#             inorder = root.val
#             root = root.right
#         return True

# @lc code=end

