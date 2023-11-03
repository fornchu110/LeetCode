<<<<<<< HEAD
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# ���@tree, return��tree�O�_�蹳���

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), recursive�ݭn��Ostack�Ŷ�
# space = O(n)��]�Orecursive��O��stack�Ŷ��N�Orecursive���`��, �b�o��N�O���̰���, �ӷ�Ҧ�node���u���@��child�ɴN�|��n
# �Q�θ��˴���tree�O�_�ۦP�������Q�k, ��root��left�Mright�X���˴���tree�O�_�蹳
# �o�D���ܤ֤@��node, �ҥH���ΧP�_root��None
class Solution:
    # same�g�b�~��, �������ӧ�
    # def same(self, p, q):
    #     if p is None and q is None:
    #         return True
    #     elif p is None or q is None:
    #         return False
    #     elif p.val!=q.val:
    #         return False
    #     else:
    #         lsub = self.same(p.left, q.right)
    #         rsub = self.same(p.right, q.left)
    #         return lsub and rsub
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # same�g�b�̭�
        def same(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            else:
                # �蹳, �]�N�O���l�n=�k�l�B�k�l=���l
                lsub = same(p.left, q.right)
                rsub = same(p.right, q.left)
                return lsub and rsub
        # ��Xroot�����kchild, recursive�U�h�P�_�O�_�蹳
        ltree = root.left
        rtree = root.right
        return same(ltree, rtree)

# By BFS(iterative), time: O(n), space: O(n)
# ���M�n�P�ɧP�_���tree, ���i�H�u�Τ@��queue����
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         rtree = root.right
#         ltree = root.left    
#         # �إ�queue
#         queue = collections.deque()
#         # �]�n�@���ݨ��tree, �ҥH�N��tree node�]���@�Ӥ���append�i�h, append�@���u��@�Ӥ���
#         # append�i�h��(rtree, ltree)�N�O��U�n�������Ӥ���
#         queue.append((rtree, ltree))
#         while queue:
#             # twonode = queue.popleft()
#             # rtree = twonode[0]
#             # ltree = twonode[1]
#             # pop�X�Ӥ@���O(r, l)�o�˪��榡, ��W���P�˷N��, �`�N���npop�⦸
#             # rtree, ltree���P��(rtree, ltree)
#             rtree, ltree = queue.popleft
#             # ��̳��ONone�N���|��child, ����continnue
#             if rtree is None and ltree is None:
#                 continue
#             elif rtree is None or ltree is None:
#                 return False
#             elif rtree.val!=ltree.val:
#                 return False
#             else:
#                 # �U�����rtree���k�l�Mltree�����l
#                 queue.append((rtree.right, ltree.left))
#                 # �H�Τ��rtree�����l�Mltree���k�l
#                 queue.append((rtree.left, ltree.right))
#         # ���Xwhile�N��queue�S�����󤸯�, �]�N�O�w�g���X�����tree, ���w�OTrue    
#         return True
        
# @lc code=end

=======
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# ���@tree, return��tree�O�_�蹳���

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), recursive�ݭn��Ostack�Ŷ�
# space = O(n)��]�Orecursive��O��stack�Ŷ��N�Orecursive���`��, �b�o��N�O���̰���, �ӷ�Ҧ�node���u���@��child�ɴN�|��n
# �Q�θ��˴���tree�O�_�ۦP�������Q�k, ��root��left�Mright�X���˴���tree�O�_�蹳
# �o�D���ܤ֤@��node, �ҥH���ΧP�_root��None
class Solution:
    # same�g�b�~��, �������ӧ�
    # def same(self, p, q):
    #     if p is None and q is None:
    #         return True
    #     elif p is None or q is None:
    #         return False
    #     elif p.val!=q.val:
    #         return False
    #     else:
    #         lsub = self.same(p.left, q.right)
    #         rsub = self.same(p.right, q.left)
    #         return lsub and rsub
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # same�g�b�̭�
        def same(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            else:
                # �蹳, �]�N�O���l�n=�k�l�B�k�l=���l
                lsub = same(p.left, q.right)
                rsub = same(p.right, q.left)
                return lsub and rsub
        # ��Xroot�����kchild, recursive�U�h�P�_�O�_�蹳
        ltree = root.left
        rtree = root.right
        return same(ltree, rtree)

# By BFS(iterative), time: O(n), space: O(n)
# ���M�n�P�ɧP�_���tree, ���i�H�u�Τ@��queue����
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         rtree = root.right
#         ltree = root.left    
#         # �إ�queue
#         queue = collections.deque()
#         # �]�n�@���ݨ��tree, �ҥH�N��tree node�]���@�Ӥ���append�i�h, append�@���u��@�Ӥ���
#         # append�i�h��(rtree, ltree)�N�O��U�n�������Ӥ���
#         queue.append((rtree, ltree))
#         while queue:
#             # twonode = queue.popleft()
#             # rtree = twonode[0]
#             # ltree = twonode[1]
#             # pop�X�Ӥ@���O(r, l)�o�˪��榡, ��W���P�˷N��, �`�N���npop�⦸
#             # rtree, ltree���P��(rtree, ltree)
#             rtree, ltree = queue.popleft
#             # ��̳��ONone�N���|��child, ����continnue
#             if rtree is None and ltree is None:
#                 continue
#             elif rtree is None or ltree is None:
#                 return False
#             elif rtree.val!=ltree.val:
#                 return False
#             else:
#                 # �U�����rtree���k�l�Mltree�����l
#                 queue.append((rtree.right, ltree.left))
#                 # �H�Τ��rtree�����l�Mltree���k�l
#                 queue.append((rtree.left, ltree.right))
#         # ���Xwhile�N��queue�S�����󤸯�, �]�N�O�w�g���X�����tree, ���w�OTrue    
#         return True
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
