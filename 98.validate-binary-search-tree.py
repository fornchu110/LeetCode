#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# 給tree判斷是否為BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n)
# 注意BST性質, 左sub tree一定比root小, 右subtree一定比root大
# float("-inf")代表負無窮大, float("inf")代表正無窮大
# 設計函數helper時就要先定義好最大範圍
class Solution:
    def helper(self, node, lower = float('-inf'), upper = float('inf')) -> bool:
        if not node:
            return True
        val = node.val
        # 代表root不在(lower, upper)內
        if val<=lower or val>=upper:
            return False
        # 左sub tree所有node.val只能在(lower, val)內才是BST
        if not self.helper(node.left, lower, val):
            return False
        # 右sub tree所有node.val只能在(val, upper)內才是BST
        if not self.helper(node.right, val, upper):
            return False
        # 代表左sub tree和右sub tree所有node.val確實都在範圍內
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        # 呼叫helper並回傳結果, 只給參數root代表不用更新lower和upper
        return self.helper(root)
    
# By inorder traversal, time: O(n), space: O(n)
# 觀察inorder traversal BST
# 發現走訪到的node.val不斷上升到走訪結束就代表是BST, 反之非BST
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         stack, inorder = [], float('-inf')
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             # 如果走訪到的新node.val小於上一個node.val, 代表不是BST
#             if root.val <= inorder:
#                 return False
#             inorder = root.val
#             root = root.right
#         return True

# @lc code=end

