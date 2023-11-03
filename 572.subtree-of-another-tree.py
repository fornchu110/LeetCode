#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By enumerate DFS, time: O(|root| x |subroot|), space: O(max{droot ,dsubroot}), d��depth
# ��root����tree���X�Htree���Ҧ�node��root��
# �O�_�s�bsubroot��root���o��tree�@��subtree
# is�O�P�_�O�����m, ==�O�P�_��, ���M�bNone�ɳ��i�H��, ��is�|������Ĳv
class Solution:
    # ��̳����U���X, ���ODFS
    # check�ΨӬݬۦP�۹��m��node.val�O�_�۵�, �۵��A�~�򩹤U
    def check(self, curRoot, curSubRoot):
        # ����tree�b�ۦP�۹��m��node.val����None�N���T
        if curRoot is None and curSubRoot is None:
            return True
        # ��@�ӬONone�@�Ӥ��O�N���i�ରsubtree
        if curRoot is None or curSubRoot is None:
            return False
        # �ݭn�W����Ӥ��ઽ���P�_curRoot.val==curSubRoot.val�O�]��None�D��, ����P�Ȱ�==�P�_
        # ��U���node�Ȭ۵��N�����i��OsubTree, �A�Ӭݥ��l��M�k�l��, ���n�۵��ҥH��and
        return curRoot.val==curSubRoot.val and self.check(curRoot.left, curSubRoot.left) and self.check(curRoot.right, curSubRoot.right)
    
    # �ΨӬݷ�Uroot�O�_�s�bsubtree, ���_�I�scheck�M�ۤv
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        # �H�쥻root��root�}�l�P�_, �YFalse�K��쥻root�����l��H�Υk�l�𰵧P�_ 
        # �u�n����@�o�{�OsubTree�Y�i�ҥH��or, �Opreorder���ǰ��P�_: root->���l->�k�l
        return self.check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# @lc code=end

