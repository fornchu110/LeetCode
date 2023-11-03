#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# By recursive, time: O(n), space: O(n), 這題不確定
# 看#1302的nonlocal說明和用法
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 把def寫在裡面可以避免函式之間多傳遞參數和使用self.來使用class下的def
        res = 0
        def dfs(node):
            # 終止條件
            # 記住node is None比not Node寫法更好, 不然會多判斷空的字串、列表、字典進來
            if node is None:
                return None
            # 判斷當下node.val是否為target
            nonlocal res
            if node.val==target.val:
                # 代表傳遞的是整個node的address, 而非只有node.val
                res = node
            # 當下判斷完, 往左子和右子繼續判斷
            dfs(node.left) 
            dfs(node.right)
        # 開始搜尋, 將cloned的root傳遞進去, 從此開始遞迴
        dfs(cloned)
        return res
        
# @lc code=end

