#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 給一個tree, 要求return照inorder走訪順序所排序的新tree, 且新tree只有右子沒左子
# 先inorder走訪tree用list存放node.val,  
class Solution(object):
    def increasingBST(self, root):
        # 用self.res保存走訪到的node
        self.res = []
        self.inOrder(root)
        if not self.res:
            return 
        dummy = TreeNode(-1)
        cur = dummy
        for node in self.res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
    # 記得
    # inorder走訪, 左子->當下node要做的操作->右子
    # preorder: 當下node要做的操作->左子->右子
    # postorder: 左子->右子->當下node要做的操作
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)
        
# @lc code=end

