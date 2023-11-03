<<<<<<< HEAD
#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# ����tree p�Mq, return �����O�_�ۦP

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P�BQ���O�N��p�Bq��node��
# min����]�O�u�n���@�̴��e�O�P�_�����N�N��false
# �����פ@�˦���ڤ����
# �P�ɹ���tree��BFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # collections����@�F�h�خe��, .deque�O����queue, [p]�N��qp��head�}�l�Np�@�ӭө�Jdeque
        # �]�i�H��deque([p, 3])�N���Jp���̦����X�쪺3��node
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            # popleft���P��list��@�ɪ�pop[0]
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val!=node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            # ��ɱ���, �Q��XOR��̬ۦP��1, ��̤��P��0���ʽ�
            # tree node�]���O�@�Ӥ@�ӱ���linklist, ���i��^�P�_, ��None�ɤS����P�_val
            # �ҥH�Q��not, ��̬��Ůɨ�̭�not���|�OTrue, �Ө�̫D�Ůɨ�̪�not���|�OFalse, �]�N�O�����P�ɱ���~����
            # �o�ؼg�k�]�i�H�Φb�}�Y�P�_return False��
            if (not left1)^(not left2):
                return False
            if (not right1)^(not right2):
                return False
            # ���lnode�N���O�[�Jqueue��, �`�N����NNone�[�J�ҥH�n�P�_
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)
        # ����o�䤣�i����䳣�٦�node, ���䳣���ŮɧƱ�return True
        # �ҥH�~��not�ӥB���ݭnXOR
        return not queue1 and not queue2

# By DFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P�BQ���O�N��p�Bq��node��
# min����]�O�u�n���@�̴��e�O�P�_�����N�N��false
# ����P�ɰ�DPS���
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # �P�ɤ�����tree�n�`�N��ɱ���, �]��None, �]�N�O��@�䬰�Ů�, �L�k���val
#         # ����䳣�ONone, ���S�����D���@��, ��True
#         if p is None and q is None:
#             return True
#         # �Q��elif�b�o�̱ư��F���䳣�O�Ū����p
#         # ����䦳��@���ťt�@�䤣���Ů�, �N���@��, ��False
#         elif p is None or q is None:
#             return False
#         # ����o��N����䳣�D��, �i�H���val, ��val���P�N���@��
#         elif p.val!=q.val:
#             return False
#         # �o��N����䳣�D�ťBval�ۦP, ���N������䪺���l�M�k�l
#         else:
#             lsub = self.isSameTree(p.left, q.left)
#             rsub = self.isSameTree(p.right, q.right)
#             # True��false, �����breturn�P�_�Y�i
#             # ���νᤩ��lsub�Mrsub���ܼƤ]�వ�P�_
#             return lsub and rsub
    
# @lc code=end

=======
#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# ����tree p�Mq, return �����O�_�ۦP

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P�BQ���O�N��p�Bq��node��
# min����]�O�u�n���@�̴��e�O�P�_�����N�N��false
# �����פ@�˦���ڤ����
# �P�ɹ���tree��BFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # collections����@�F�h�خe��, .deque�O����queue, [p]�N��qp��head�}�l�Np�@�ӭө�Jdeque
        # �]�i�H��deque([p, 3])�N���Jp���̦����X�쪺3��node
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            # popleft���P��list��@�ɪ�pop[0]
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val!=node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            # ��ɱ���, �Q��XOR��̬ۦP��1, ��̤��P��0���ʽ�
            # tree node�]���O�@�Ӥ@�ӱ���linklist, ���i��^�P�_, ��None�ɤS����P�_val
            # �ҥH�Q��not, ��̬��Ůɨ�̭�not���|�OTrue, �Ө�̫D�Ůɨ�̪�not���|�OFalse, �]�N�O�����P�ɱ���~����
            # �o�ؼg�k�]�i�H�Φb�}�Y�P�_return False��
            if (not left1)^(not left2):
                return False
            if (not right1)^(not right2):
                return False
            # ���lnode�N���O�[�Jqueue��, �`�N����NNone�[�J�ҥH�n�P�_
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)
        # ����o�䤣�i����䳣�٦�node, ���䳣���ŮɧƱ�return True
        # �ҥH�~��not�ӥB���ݭnXOR
        return not queue1 and not queue2

# By DFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P�BQ���O�N��p�Bq��node��
# min����]�O�u�n���@�̴��e�O�P�_�����N�N��false
# ����P�ɰ�DPS���
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # �P�ɤ�����tree�n�`�N��ɱ���, �]��None, �]�N�O��@�䬰�Ů�, �L�k���val
#         # ����䳣�ONone, ���S�����D���@��, ��True
#         if p is None and q is None:
#             return True
#         # �Q��elif�b�o�̱ư��F���䳣�O�Ū����p
#         # ����䦳��@���ťt�@�䤣���Ů�, �N���@��, ��False
#         elif p is None or q is None:
#             return False
#         # ����o��N����䳣�D��, �i�H���val, ��val���P�N���@��
#         elif p.val!=q.val:
#             return False
#         # �o��N����䳣�D�ťBval�ۦP, ���N������䪺���l�M�k�l
#         else:
#             lsub = self.isSameTree(p.left, q.left)
#             rsub = self.isSameTree(p.right, q.right)
#             # True��false, �����breturn�P�_�Y�i
#             # ���νᤩ��lsub�Mrsub���ܼƤ]�వ�P�_
#             return lsub and rsub
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
