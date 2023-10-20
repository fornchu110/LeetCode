#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# ���@binary search tree�M��node p�Bq, return�L�̪��̧C�@�P����
# �̧C�@�P�����N�O���׳̱�����I���@�P����, �O�o�n�^��node�ӫDint

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# By iterative, time: O(n), space: O(1)
# �ھګe���[���@�P�������ʽ�N�O�@�P���|���̫�@�ӬۦPnode��, �N�F�Ѩ��i�H�P�ɨ��Xp�Mq
# Ex: p = 4: [6, 2, 4], q = 2: [6, 2]
# �ҥH�ϥ�while�j��, ��p�Mq���U��node�p�ɩ�����, �j�ɩ��k��
# �������~�N�N��w�g�S���@�P���|�i�H���U��, break
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ��l��res��root
        res = root
        while True:
            # �u�n���~�򨫳X�N���~�򦳦@�P���|, �����״N��s���s���X��node
            if p.val<res.val and q.val<res.val:
                res = res.left
            elif p.val>res.val and q.val>res.val:
                res = res.right
            # �S���@�P���|�ਫ�U�h�F�Nbreak
            else:
                break
        return res

# By recursive, time: O(n), space: O(n)
# �i�H�o�{�ƻ�s���@�P����?�N�O�ΦP�˪��覡���X�h�d����node��, ���|�̳̫�@�ӬۦP��node
# Ex: ��2���|:[6, 4, 2], ��4���|: [6, 4], ��4�N�O4�M2���@�P����
# �]�����O�d���node�o����|��, ���X���|��̫�@�ӬۦPnode�Y�i
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def DFS(node, target):
#             # �|��s�b�W�h�禡�w�q��path�ҥH��nonlocal
#             nonlocal path
#             if node is None:
#                 return
#             # �o�D�nreturn node, �ҥH���|�̬O��node
#             path.append(node)
#             # ����ؼ�node�F�N���~�򨫳X
#             if node.val==target.val:
#                 return
#             # �ؼФ�ثenode�p���N�������X
#             if node.val>target.val:
#                 DFS(node.left, target)
#             # �ؼФ�ثenode�j���N���k���X
#             elif node.val<target.val:
#                 DFS(node.right, target)
#         path = []
#         # p�Mq���Onode
#         DFS(root, p)
#         p_path = path
#         path = []
#         DFS(root, q)
#         q_path = path
#         # ��zip�P�ɨ��X��Ӹ��|
#         for i, j in zip(p_path, q_path):
#             if i.val==j.val:
#                 res = i
#             # �@�J�줣�ۦP��node�Nbreak
#             else:
#                 break
#         return res

# @lc code=end

