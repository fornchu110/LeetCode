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
# 求出BST中所有node自己之val+右方tree val之值, 因是BST所以右方都是value比自己大之node
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tmp = 0
        def dfs(node):
            if node is not None:
                # 中進來, 右邊的node都把value做總並更新過, 才輪到左邊的node
                nonlocal tmp
                dfs(node.right)
                tmp += node.val
                node.val = tmp
                dfs(node.left)
        # 從root開始走訪, 中->右->左
        dfs(root)
        return root
        
# @lc code=end

