#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), space�Orecursive�Ҫ�O��stack, ��tree�̤j����
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # �פ����, ��order���ŮɥN���Onode
        if not inorder or not postorder:
            return None
        # root���w�Opostorder�̫�@�Ӥ���
        root_val = postorder[-1]
        # �إ�root node
        root = TreeNode(root_val)
        # ��Xroot�binorder����index, index�H���O��sub tree, �H�k�O�ksub tree
        midIndex = inorder.index(root_val)

        # ��Xinorder�U����sub tree�M�ksub tree
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex+1:]

        # ��Xpostorder�U����sub tree�M�ksub tree, ���׳��|�Minorder�۵�
        # postorder: ��->�k->root
        postorderLeft = postorder[: len(inorderLeft)]
        # -1�O�]���̫ᥲ�w�Oroot
        postorderRight = postorder[len(inorderLeft):len(inorder)-1]
        # recursive���G�N�O��Unode����child�M�kchild
        # recursive ��sub tree
        root.left = self.buildTree(inorderLeft, postorderLeft)
        # recursive �ksub tree
        root.right = self.buildTree(inorderRight, postorderRight)
        # �Q���@�Urecursive������j, child���T�{�F�~�౵��parent�W
        # �ҥH�b�̫�@��~��root��left�Mright child���W
        # �ҥH���M�Oreturn root, root�w�g�z�L�W����recursive�M��Lnode���p�_��
        return root

# @lc code=end

