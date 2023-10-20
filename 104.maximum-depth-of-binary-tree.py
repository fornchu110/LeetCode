#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# ���@�ӤG����, return���𪺳̲`����, root���� = 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS(recursive) , time: O(n), space: O(h), h��tree��, �]recursive�ݭnstack, ��stack�j�p���Mrecursive���`��, ���a��p�N�OO(n)
# ��dfs���Xnode, �̫�Nlev�̲`��return�Y�i
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # �ۤv���g�k, �ϥ�nonloval
        # is�ΨӧP�_�O�����m, ==�ΨӧP�_��
        if root is None:
             return 0
        # res��l�Ƭ�0
        res = 0
        def dfs(node, lev):
            if node==None:
                return None
            # �]dfs�o�Ө禡�n���W�@�h, �]�N�OmaxDepth�o�өҩw�q���ܼ�res
            # �]���n���Nres�ŧi��nonlocal
            # �p�Gres�O�bsolution�~�]�N�Oglobal, ���N�n�令�ŧiglobal res�~��ק�
            nonlocal res
            # ���X��F�s���@�hnode, �ҥHlev+1
            lev += 1
            max(res, lev)
            dfs(node.left, lev)
            dfs(node.right, lev)
        # ����lev�q0�}�l?��lev�Q�����Xnode���e�Ҿ֦�������
        dfs(root, 0)
        return res

        #²��g�k, ���μg�B�~�禡
        # if root is None:
        #     # �o�̦P�ɾ���l�ƨS���I=����0�o���
        #     return 0
        # # ���_���jmaxDeapth�Y�i
        # l_depth = self.maxDepth(root.left)
        # r_depth = self.maxDepth(root.right)
        # # ���tree�����״N�O�ltree���󰪪�+1
        # return max(l_depth, r_depth)+1

# By BFS(iterative), time: O(n), space: O(n)
# space = O(n)�O�]�����@queue��O���Ŷ�
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # ��tree���״N�O0
#         if root == None:
#             return 0
#         # ��l��queue�M����, �D��tree�ɱqroot�}�l���X
#         # �o�̪�queue��ڤW�N�O��list����, �q�Lappend�[�J����, pop(0)�N�Y�ݮ��X
#         # �N��list�]�������stack
#         queue = [root]
#         depth = 0
#         # ��queue�D��, �]�N�O�٦�node�����X
#         while queue:
#             # ��elevel��node��
#             n = len(queue)
#             # �N��elevel��node�@�Ӥ@�ӳB�z
#             for i in range(n):
#                 node = queue.pop(0)
#                 # �p�G�����l�N�N���l��Jqueue
#                 if node.left:
#                     queue.append(node.left)
#                 # �p�G���k�l�N�N�k�l��Jqueue
#                 if node.right:
#                     queue.append(node.right)
#             # ��elevel��node pop���N�����o�h, ��U�@�h�ҥH�n+1
#             depth += 1
#         return depth

# @lc code=end

