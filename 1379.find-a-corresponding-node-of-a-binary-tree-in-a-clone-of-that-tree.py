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

# By recursive, time: O(n), space: O(n), �o�D���T�w
# ��#1302��nonlocal�����M�Ϊk
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # ��def�g�b�̭��i�H�קK�禡�����h�ǻ��ѼƩM�ϥ�self.�Өϥ�class�U��def
        res = 0
        def dfs(node):
            # �פ����
            # �O��node is None��not Node�g�k��n, ���M�|�h�P�_�Ū��r��B�C��B�r��i��
            if node is None:
                return None
            # �P�_��Unode.val�O�_��target
            nonlocal res
            if node.val==target.val:
                # �N��ǻ����O���node��address, �ӫD�u��node.val
                res = node
            # ��U�P�_��, �����l�M�k�l�~��P�_
            dfs(node.left) 
            dfs(node.right)
        # �}�l�j�M, �Ncloned��root�ǻ��i�h, �q���}�l���j
        dfs(cloned)
        return res
        
# @lc code=end

