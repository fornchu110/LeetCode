#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By predecessor, time: O(n), space: O(1)
# �[��preorder�Oroot->��->�k��, �o�{���l��̥k��node�Q���X��~�}�l���X�k�l��
# �ҥH���l��̥knode�Y�O�k�l��root��predecessor(�e�X�`�I)
# �@�k�N�O���cur���l�̥knode��Nroot�k�l���W�h
class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                predecessor = nxt = cur.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right

# By recursive, time: O(n), space: O(n)
# ����preorder���X��O���U�Ӷ���, �A�Nnode��������m�W
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         # ����preorder���G
#         preorderList = list()
#         # ��preorder���X
#         def preorderTraversal(root: TreeNode):
#             if root:
#                 #preorder����:root����->���l��->�k�l��
#                 preorderList.append(root)
#                 preorderTraversal(root.left)
#                 preorderTraversal(root.right)
        
#         preorderTraversal(root)
#         size = len(preorderList)
#         # ���N�覡�վ�node
#         for i in range(1, size):
#             prev, curr = preorderList[i - 1], preorderList[i]
#             prev.left = None
#             prev.right = curr

# @lc code=end

