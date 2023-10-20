#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# ���@��tree, �Ʊ氵��Hroot�����߱N���k�l��洫

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), space�Ӧ�recursive��stack����
# �]tree�i��skewed�]�N�O�u����child�Υu���kchild, �ҥH���a���p����n, �N���recursive n��, �ҥHspace = O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #input�O�H�@��array�x�s��tree��root
        #�ҥH�`�Ninput���O�@��array, �ӬO�@��root node
        #�ҥH��ڤW�L��array�����Ƨ�, �D�ؤw�g��node���������Y�]�w�n�F, �����ϥΧY�i
        #�]���O���j, �ҥH�ݭn�פ����, ����Dnode�ɰ���
        if not root:
            return root    
        #�Ninput���Ҧ�node���j�U�h
        #�]�N�O�C��@�Ӹ`�I�N��@root,�N�䥪�l�I�M�k�l�I��root���l��½��
        #Ū�쥪�l�I
        left = self.invertTree(root.left)
        #Ū��k�l�I
        right = self.invertTree(root.right)
        #�N�s�����l�I�t���쥻���k�l�I, �N�s���k�l�I�t���쥻�����l�I
        root.left, root.right = right, left
        #retrun�ɦ^�ǤF�@�Ӥw�g�����洫��node
        #�]�N�O���q�̫�@�hnode�}�l, �N�洫����node�^�ǵ���parent, ����^�ǯu����root�ɵ���
        return root

# @lc code=end

