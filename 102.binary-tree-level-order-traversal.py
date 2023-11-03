#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# ���@��tree, �n�Dretrun���U�Ӥ����O�P�@level��node.val
# Ex: 1�Olevel1, 9�B10�Olevel2, return:[[1], [9, 10]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS(iterative), time: O(n), space: O(n)
# �n�ھ�level�N�O��BFS, �u�O�n�`�N�p��`���Plevel�����M���append
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        # �Nroot�s�W�iqueue
        queue = collections.deque([root])
        res = []
        # ��queue�٦������N��|�����X��
        # ��ڤW�C�����@��level�|�^��while�o��
        while queue:
            # �Plevel�������n��b�@�_
            tmp = []
            # n�N��۳o�@level�������ƶq
            n = len(queue)
            for i in range(n):
                # pop n��, �]�N�O��Plevel�Ҧ�node���B�z
                node = queue.popleft()
                # �[�Jtmp
                tmp.append(node.val)
                ltree = node.left
                rtree = node.right
                # �p�G��child�N��Jqueue
                if ltree:
                    queue.append(ltree)
                if rtree:
                    queue.append(rtree)
            # ����for�N��ۤ@��level����, �Ntmp�[�Jres
            res.append(tmp)
        return res
        
# @lc code=end

