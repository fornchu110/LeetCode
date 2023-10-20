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

# �ѤU�ӤW��tree���Ҧ�node���U�C�B��
# node.val=1��0�N��true��false, 2��3�N��索�kchild��or��and
# �̫�return�Otrue��false

# By recursive, time: O(n), space: O(n)
# ���j�U�h���̫�^�ǵ��G�Y�i
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # �פ����, �Ҧ�node���O0�N�O2��child, �ҥH�u�n�˴���@�O�_�s�b�Y�i
        # �o���i�H�ݰ��e�Ǩ��X(preorder traversal), �b�o���t�~��ب��X�٤U�������
        if root.left is None:
            return root.val
        # 2�N��@or
        if root.val==2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # else�N��3, ��and
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
# @lc code=end

