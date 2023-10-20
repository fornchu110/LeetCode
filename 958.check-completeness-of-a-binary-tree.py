#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# ���@��tree, �Ytree�Ocomplete tree return True, ���Ocomplete tree return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS and node index, time: O(n), space: O(n)
# perfect tree�N��C��node�u�n��child���w�|�����, ���O�@�ӤT����
# full tree�N���Fleaf�~�Ҧ�node���|�����child, ���i��̫�@�h���a��
# complete tree�h�N��̫�@��level���@�w�|����, �Dleaf�]�i��u��1��child, ���̫�@�h�����a��
# perfect = full and complete
# �P�_complete tree�覡�N�O�@�h�@�h��index, ��index�����P�ثetree����node�ƮɥN��Dcomplete
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # root��index�O1
        idx = 1
        cnt = 0
        queue = collections.deque()
        # �Nroot�M��index�]���@�Ӥ����[�Jqueue
        queue.append((root, idx))
        # BFS�Hlevel���X, �u�n�٦�node�bqueue�N��|�����X��
        while queue:
            (node, idx) = queue.popleft()
            # pop�@��node���P�ɥN����@��node, cnt�W�[
            cnt += 1
            # ��node�Ƥ����Pindex�N��Dcomplete
            if cnt!=idx:
                return False
            # �קKnode��None
            if node.left:
                # ���l��index�Oparent idx*2
                queue.append((node.left, 2*idx))
            if node.right:
                # �k�l��index�Oparent idx*2+1
                queue.append((node.right, 2*idx+1))
        return True
        
# @lc code=end

