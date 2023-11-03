#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive
class Solution:
    def inOrder(self, root:TreeNode, res):
        #���j���פ����, ��Dnode�ɤ��λ��j
        if root == None:
            return
        #inorder�O��->��->�k, �ҥH��C��node���O�q����}�l���j
        #���索�l�𰵻��j
        self.inOrder(root.left, res)
        #���l�𻼰j������~�|����root
        #�Nroot��Jres
        res.append(root.val)
        #���l�𪺳����Mroot������, �A��k�l�𰵻��j
        self.inOrder(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #�]�^�Ǫ��O�}�C, �B��u���@��node�ɭn�^�Ǫ�, �ҥH��l�Ƥ@�Ӱ}�C
        #�qroot�}�l��tree���C��node�U�h���j, �C���H��ɪ�node��root��inorder
        res = []
        #�}�l��inorder�l��
        self.inOrder(root, res)
        return res

# By stack
# #���recursive�N���stack��
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         #���@�@�ӥs��stack��list
#         # �]��append�O�q�̧��ݥ[�J��i���, ��pop�O�N�̧��ݸ�ƨ��X
#         # ��Ӱt�X�Y�i�F����i���X��stack
#         stack = []
#         res = []
#         while root or stack:
#             if root:
#                 stack.append(root)
#                 root = root.left
#             else:
#                 cur = stack.pop()
#                 res.append(cur.val)
#                 root = cur.right
#         return res

# @lc code=end

