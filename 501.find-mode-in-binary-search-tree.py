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

# ��XBST���X�{���Ƴ̦h��node.val

# By DFS, time: O(n), space: O(logn), logn�O�ѩ�recursive�Ҫ�O��stack�Ŷ�
# ��DFS���X�L�{�`�N�Ѥp����j(inorder ���l->root->�k�l), �O���W���ݨ쪺node.val�H�η�Unode.val�X�{������, �٦��̱`�X�{��node.val
# ���X�L�{�ݨ��W��node�@�˪��N���ƴNcnt+1, �p�G�X�{���ƶW�L�ثe�X�{�̦h��������most, �h��smost�Mres
class Solution:
    def __init__(self):
        # ����recursive�L�{�һݭn��s����T
        self.res = []
        self.most = 0
        self.last = None
        self.cnt = 0

    def inorder(self, node):
        if node is None:
            return 
        # ��subtree�n��recursive��
        if node.left:
            self.inorder(node.left)
        # �B�zroot
        if node.val==self.last:
            self.cnt += 1
        # �����ƨ��o�ӷs��node�u�X�{�@��
        else:
            self.cnt =  1
        # �p�G�X�{���ƶW�L�ثe�̦h��
        if self.cnt==self.most:
            self.res.append(node.val)
        # �p�G�ثe�o��node�X�{���Ƥ񤧫e�̦h���٦h
        elif self.cnt>self.most:
            # ��smost
            self.most = self.cnt
            # �N�s��node.value�[�i
            self.res.append(node.val)
        self.last = node.val
        # recursive�ksubtree
        if node.right:
            self.inorder(node.right)

    def findMode(self, root: TreeNode) -> List[int]:
        # �qroot�U�hrecursive
        self.inorder(root)
        return self.res

# @lc code=end

