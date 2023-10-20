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

# ���@��tree, �n�Dreturn��inorder���X���ǩұƧǪ��stree, �B�stree�u���k�l�S���l
# ��inorder���Xtree��list�s��node.val,  
class Solution(object):
    def increasingBST(self, root):
        # ��self.res�O�s���X�쪺node
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
    # �O�o
    # inorder���X, ���l->��Unode�n�����ާ@->�k�l
    # preorder: ��Unode�n�����ާ@->���l->�k�l
    # postorder: ���l->�k�l->��Unode�n�����ާ@
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)
        
# @lc code=end

