#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# By dfs, time: O(n), space: O(n)
# �N������val�����Ƥ�node.val�[�`return
# �]���n�O�������Mparent��value���Ѽƶǻ�
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        # �����Mparent��val���n��Ѽƶǻ��~��P�_
        def dfs(gp_val, p_val, node):
            if not node:
                return
            # �P�_����.val�����Ʈ�, �N�ۨ�val�[�`
            if gp_val&1 == 0:
                nonlocal res
                res += node.val
            # ���U���w, ���ɦۨ���parent�ܦ�child������, �ۨ��ܦ�child��parent
            dfs(p_val, node.val, node.left)
            dfs(p_val, node.val, node.right)
        # root�S��parent�M����, ��l�Ʀ�-1���v�T�P�_
        dfs(-1, -1, root)
        return res

# By bfs, time: O(n), space: O(n)
# bfs�����k�n���@queue�~�ા�D�ثelevel�O�_���X����
# class Solution:
#     def sumEvenGrandparent(self, root: TreeNode) -> int:
#         q = collections.deque([root])
#         res = 0
#         while len(q) > 0:
#             node = q.popleft()
#             if node.val&1 == 0:
#                 if node.left:
#                     if node.left.left:
#                         res += node.left.left.val
#                     if node.left.right:
#                         res += node.left.right.val
#                 if node.right:
#                     if node.right.left:
#                         res += node.right.left.val
#                     if node.right.right:
#                         res += node.right.right.val
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         return res

# @lc code=end

