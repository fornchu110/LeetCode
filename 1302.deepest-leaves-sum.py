#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive and nonlocal, time: O(n), space: O(n)
# �n�Nleave��val�[�`��return, �ϥ�DFS���覡���j���X���tree
# ���I�b��p��ǻ��[�`�᪺��res�H�Ψ��X
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # �ϥΨ�maxLeval�P�_leave, res�ΨӰO��leave�`�M
        maxLevel, res = -1, 0
        def dfs(node: Optional[TreeNode], level: int) -> None:
            # �פ����
            # �O��node is None��not Node�g�k��n, ���M�|�h�P�_�Ū��r��B�C��B�r��i��
            if node is None:
                return
            # ��禡���ק�W�@�h�禡��local variable�O��nonlocal
            # �o��N�O�]���ϥΨ�def deepestLeavesSum�ŧi��maxLevel�Mres
            # �Y�Oglobal variable(�̥~�h)���i�A��nonlocal, �h���@�|
            # �禡���ק�global variable�~��global, �קK�ŧi�èϥΨ�@�ӷs��local variable
            # global�ŧi�O�L�׫e�᪺, nonlocal�h�_
            # �`�N��¨ϥ����ӬO�����B�~�ŧi��
            nonlocal maxLevel, res
            # �p�G��U���h�Ƥ񤧫e��������`, �N���e��node�����|�Oleave
            # ���sassign maxLevel�Mres
            if level>maxLevel:
                maxLevel, res = level, node.val
            # �h�Ƴ̲`��node�@�w�Oleave, �ҥH����̲`����X�ӥ[�`
            elif level==maxLevel:
                res += node.val
            # �o�h���X��, ���U�@�h
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        # �N�h�Ʒ�@�Ѽƶǻ�, �@�䨫�X�@�䪾�D��ĴX�h
        dfs(root, 0)
        return res
        
# @lc code=end

