#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 找出BST中出現次數最多的node.val

# By DFS, time: O(n), space: O(logn), logn是由於recursive所花費的stack空間
# 用DFS走訪過程注意由小走到大(inorder 左子->root->右子), 記錄上次看到的node.val以及當下node.val出現的次數, 還有最常出現的node.val
# 當走訪過程看到跟上個node一樣的代表重複就cnt+1, 如果出現次數超過目前出現最多次的紀錄most, 則更新most和res
class Solution:
    def __init__(self):
        # 紀錄recursive過程所需要更新的資訊
        self.res = []
        self.most = 0
        self.last = None
        self.cnt = 0

    def inorder(self, node):
        if node is None:
            return 
        # 左subtree要先recursive完
        if node.left:
            self.inorder(node.left)
        # 處理root
        if node.val==self.last:
            self.cnt += 1
        # 不重複那這個新的node只出現一次
        else:
            self.cnt =  1
        # 如果出現次數超過目前最多次
        if self.cnt==self.most:
            self.res.append(node.val)
        # 如果目前這個node出現次數比之前最多的還多
        elif self.cnt>self.most:
            # 更新most
            self.most = self.cnt
            # 將新的node.value加進
            self.res.append(node.val)
        self.last = node.val
        # recursive右subtree
        if node.right:
            self.inorder(node.right)

    def findMode(self, root: TreeNode) -> List[int]:
        # 從root下去recursive
        self.inorder(root)
        return self.res

# @lc code=end

