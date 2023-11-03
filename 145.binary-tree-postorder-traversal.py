#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#By recursive
class Solution:
    def postorder(self, root:TreeNode, res):
        #遞迴終止條件, 若非node不用遞迴
        if not root:
            return
        #後序:左->右->中
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)
        return

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #初始化要回傳的陣列res
        res = list()
        #從root開始對所有node做後序追蹤
        self.postorder(root, res)
        #對所有node的遞迴完成, 回傳結果
        return res

# @lc code=end

