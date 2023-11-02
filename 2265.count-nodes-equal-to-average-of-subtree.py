#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# �p��node.val=�ۤv+�ۤv�Ҧ�child��value�����Ƥ�node�ƶq
# �o���D�ت��򥻤@�w�O��recursive��dfs���X�Ҧ�node���p��

# By DFS, Time: O(n), Space: O(logn)
# space = O(logn)�O�]��Recursive��stack��O���Ŷ�, ���o�D�u�O�G���𦳥i��̮tO(n), �ҥHO(height), height = �𰪤���ǽT
# ��DFS�U�h�u�O�n�P�ɰO���M�M�ثe���L���ƶq, �@���^�Ǩ�ӰѼ�
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root: Optional[TreeNode]):
            # �]�Ψ�dfs�W�@�h���averageOfSubtree�ҩw�q��res
            # �ҥH�ϥ�nonlocal, �o�˴N��ק�res�F
            # ���Q��nonlocal���ܧ�res����self.res
            nonlocal res 
            if not root:
                return 0, 0
            #�索�k�l�𰵻��j
            lsub = dfs(root.left)
            rsub = dfs(root.right)
            # �D�X�ۤv+�ۤv�Ҧ�child��value�M
            value = lsub[0]+rsub[0]+root.val
            # �D�X�ۤv+�ۤv�Ҧ�child��node�ƶq
            count = lsub[1]+rsub[1]+1
            # �ݦۤv��value�O�_�ۤv+�ۤv�Ҧ�child��value������
            # �Y�۵��h+1
            if root.val == value // count:
                res += 1
            return value, count    
        dfs(root)
        return res
    
# By DFS, Time: O(n), Space: O(logn)
# �令�Ndef�Mres�g�bclass�U
# class Solution:
#     def __init__(self):
#         self.res = 0
    
#     def dfs(self, root):
#         if not root:
#             return 0, 0
#         lsub = self.dfs(root.left)
#         rsub = self.dfs(root.right)
#         value = lsub[0]+rsub[0]+root.val
#         count = lsub[1]+rsub[1]+1
#         if root.val==value//count:
#             self.res += 1
#         return value, count

#     def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
#         self.dfs(root)
#         return self.res

             
# @lc code=end

