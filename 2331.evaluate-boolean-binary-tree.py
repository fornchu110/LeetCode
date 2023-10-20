#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 由下而上對tree中所有node做下列運算
# node.val=1或0代表true或false, 2或3代表對左右child做or或and
# 最後return是true還false

# By recursive, time: O(n), space: O(n)
# 遞迴下去做最後回傳結果即可
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # 終止條件, 所有node不是0就是2個child, 所以只要檢測其一是否存在即可
        # 這其實可以看做前序走訪(preorder traversal), 在這邊比另外兩種走訪省下比較次數
        if root.left is None:
            return root.val
        # 2代表作or
        if root.val==2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # else代表3, 做and
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
# @lc code=end

